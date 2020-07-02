//variable "project_tag" {
//  description = "Tag name to use on the project..."
//  default = "flask-app-ec2-instances"
//}
//
//resource "aws_iam_role" "ec2_role_flask_application" {
//  name = "ec2-role-flask-application"
//
//  assume_role_policy = <<EOF
//{
//  "Version": "2012-10-17",
//  "Statement": [
//    {
//      "Sid": "",
//      "Effect": "Allow",
//      "Principal": {
//        "Service": [
//          "ec2.amazonaws.com"
//        ]
//      },
//      "Action": "sts:AssumeRole"
//    }
//  ]
//}
//EOF
//
//  tags = {
//    Name = var.project_tag
//  }
//}
//
//resource "aws_iam_role_policy_attachment" "ec2_full_access_policy_attachment" {
//  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2FullAccess"
//  role = aws_iam_role.ec2_role_flask_application.name
//}
