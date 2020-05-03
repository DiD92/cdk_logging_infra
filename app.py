#!/usr/bin/env python3

import os

from aws_cdk import core
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_kinesisfirehose as firehose
import aws_cdk.aws_elasticsearch as es


class LoggignResources(core.Stack):
    def __init__(self, *args, **kwargs):
        super(LoggignResources, self).__init__(*args, **kwargs)

        # Netowrk
        self.vpc = ec2.Vpc(self, 'logging-vpc')

        self.backup_bucket = s3.Bucket(self, 'logging-backup', 
            bucket_name='logging-backup-bucket')

        self.elastic_domain = es.CfnDomain(self, 'logging-es-cluster')

        self.stream = firehose.CfnDeliveryStream(self, 'logging-stream',
            delivery_stream_name='logging-stream-firehose',
            delivery_stream_type='DirectPut', 
            elasticsearch_destination_configuration=self.elastic_domain,
            s3_destination_configuration=self.backup_bucket)

class LoggingApp(core.App):
    def __init__(self, *args, **kwargs):
        super(LoggingApp, self).__init__(*args, **kwargs)

        self.logging_resources = LoggignResources(self, 'logging-resources')

app = LoggingApp()
app.synth()