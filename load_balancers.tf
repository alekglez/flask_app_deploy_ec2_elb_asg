provider "aws" {
  region = "us-east-1"
}

data "aws_vpc" "default" {
  default = true
}

data "aws_subnet_ids" "all" {
  vpc_id = data.aws_vpc.default.id
}

data "aws_security_group" "default" {
  vpc_id = data.aws_vpc.default.id
  name   = "default"
}

data "aws_elb_service_account" "main" {}

resource "aws_s3_bucket" "lb_flask_app_access_logs" {
  bucket = "lb-flask-app-access-logs"
  force_destroy = true
  acl = "private"

  policy = <<POLICY
{
  "Id": "Policy",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "s3:PutObject"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::lb-flask-app-access-logs/*",
      "Principal": {
        "AWS": [
          "${data.aws_elb_service_account.main.arn}"
        ]
      }
    }
  ]
}
POLICY
}

resource "aws_lb" "flask_app_load_balancer" {
  name = "flask-app-load-balancer"
  load_balancer_type = "application"

  subnets = data.aws_subnet_ids.all.ids
  security_groups = [aws_security_group.security_group_elb.id]

  enable_cross_zone_load_balancing = true
  enable_http2 = true
  internal = false

  access_logs {
    bucket  = aws_s3_bucket.lb_flask_app_access_logs.bucket
    prefix  = "lb-flask-app"
    enabled = true
  }

  tags = {
    Environment = "production"
  }
}

resource "aws_lb_listener" "lb_port_80_listener" {
  load_balancer_arn = aws_lb.flask_app_load_balancer.arn
  protocol = "HTTP"
  port = 80

  default_action {
    target_group_arn = aws_alb_target_group.flask_app_ec2_target_group.arn
    type = "forward"
  }
}
