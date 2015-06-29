# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< .merge_file_8VvmhW
        ('shares', '0004_sharetransfer_current_share_price'),
        ('members', '0002_auto_20150617_0905'),
        ('savings', '0004_auto_20150526_1810'),
        ('contenttypes', '0001_initial'),
=======
        ('members', '__first__'),
>>>>>>> .merge_file_SQy3KW
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('approval_date', models.DateField()),
                ('amount', models.BigIntegerField()),
                ('payment_period', models.IntegerField()),
                ('security_details', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LoanApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('application_number', models.CharField(max_length=100)),
                ('application_date', models.DateField()),
                ('amount', models.BigIntegerField()),
                ('payment_period', models.IntegerField(max_length=11)),
                ('status', models.CharField(default=b'pending', max_length=25, choices=[(b'pending', b'Pending'), (b'approved', b'Approved'), (b'rejected', b'Rejected')])),
                ('security_details', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LoanType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('interest', models.FloatField()),
                ('interest_period', models.CharField(default=b'year', max_length=50, choices=[(b'year', b'per anum'), (b'month', b'per month'), (b'day', b'per day')])),
                ('processing_period', models.IntegerField()),
                ('minimum_amount', models.BigIntegerField()),
                ('maximum_amount', models.BigIntegerField()),
                ('minimum_membership_period', models.IntegerField()),
                ('minimum_share', models.IntegerField()),
                ('minimum_savings', models.BigIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
<<<<<<< .merge_file_8VvmhW
=======
                ('security_type', models.IntegerField(choices=[(b'shares', 1), (b'savings', 2), (b'item', 3)])),
>>>>>>> .merge_file_SQy3KW
                ('attached_to_loan', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SecurityArticle',
            fields=[
                ('security_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='loans.Security')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('identification_type', models.CharField(max_length=100)),
                ('identification', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('loans.security',),
        ),
        migrations.CreateModel(
            name='SecuritySavings',
            fields=[
                ('security_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='loans.Security')),
                ('savings_amount', models.BigIntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=('loans.security',),
        ),
        migrations.CreateModel(
            name='SecurityShares',
            fields=[
                ('security_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='loans.Security')),
                ('number_of_shares', models.IntegerField()),
                ('value_of_shares', models.BigIntegerField()),
                ('guarantor', models.ForeignKey(to='members.Member')),
<<<<<<< .merge_file_8VvmhW
                ('share_type', models.ForeignKey(to='shares.ShareType')),
=======
                ('security', models.ForeignKey(related_name='Shares Security', to='loans.Security')),
>>>>>>> .merge_file_SQy3KW
            ],
            options={
                'abstract': False,
            },
            bases=('loans.security',),
        ),
<<<<<<< .merge_file_8VvmhW
        migrations.AddField(
            model_name='security',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_loans.security_set+', editable=False, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='security',
            field=models.ManyToManyField(to='loans.Security', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='type',
            field=models.ForeignKey(to='loans.LoanType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loan',
            name='application',
            field=models.ForeignKey(to='loans.LoanApplication'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loan',
            name='guarantors',
            field=models.ManyToManyField(related_name='Guarantors', to='members.Member'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loan',
            name='loan_type',
            field=models.ForeignKey(to='loans.LoanType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loan',
            name='member',
            field=models.ForeignKey(to='members.Member'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loan',
            name='security',
            field=models.ManyToManyField(to='loans.Security', null=True, blank=True),
            preserve_default=True,
        ),
=======
>>>>>>> .merge_file_SQy3KW
    ]
