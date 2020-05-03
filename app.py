#!/usr/bin/env python3

from aws_cdk import core

from logging_cdk.logging_cdk_stack import LoggingCdkStack


app = core.App()
LoggingCdkStack(app, "logging-cdk")

app.synth()
