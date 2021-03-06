# Generated by Django 4.0.4 on 2022-06-16 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='is_admin',
            new_name='is_staff',
        ),
        migrations.AddField(
            model_name='profile_akpugo',
            name='email',
            field=models.EmailField(max_length=255, null=True, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='account_bank',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Account Bank'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='account_num',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Account number'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='campus',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='history',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Brief History'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='phone_num',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='campus',
            field=models.CharField(choices=[('Akpugo', 'Akpugo'), ('Elele', 'Elele'), ('Okija', 'Okija'), ('National', 'National'), ('None', 'None')], max_length=255, verbose_name='campus'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=255, null=True, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='executive_akpugo',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_akpugo', to='account.profile_akpugo'),
        ),
        migrations.AlterField(
            model_name='executive_elele',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_elele', to='account.profile_elele'),
        ),
        migrations.AlterField(
            model_name='executive_elele',
            name='session',
            field=models.CharField(blank=True, choices=[('1999/2000', '1999/2000'), ('2000/2001', '2000/2001'), ('2001/2002', '2001/2002'), ('2002/2003', '2002/2003'), ('2003/2004', '2003/2004'), ('2004/2005', '2004/2005'), ('2005/2006', '2005/2006'), ('2006/2007', '2006/2007'), ('2007/2008', '2007/2008'), ('2008/2009', '2008/2009'), ('2009/2010', '2009/2010'), ('2010/2011', '2010/2011'), ('2011/2012', '2011/2012'), ('2012/2013', '2012/2013'), ('2013/2014', '2013/2014'), ('2014/2015', '2014/2015'), ('2015/2016', '2015/2016'), ('2016/2017', '2016/2017'), ('2017/2018', '2017/2018'), ('2018/2019', '2018/2019'), ('2019/2020', '2019/2020'), ('2020/2021', '2020/2021'), ('2021/2022', '2021/2022'), ('2022/2023', '2022/2023')], max_length=255, verbose_name='Session'),
        ),
        migrations.AlterField(
            model_name='executive_national',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_national', to='account.profile_national'),
        ),
        migrations.AlterField(
            model_name='executive_national',
            name='session',
            field=models.CharField(blank=True, choices=[('1999/2000', '1999/2000'), ('2000/2001', '2000/2001'), ('2001/2002', '2001/2002'), ('2002/2003', '2002/2003'), ('2003/2004', '2003/2004'), ('2004/2005', '2004/2005'), ('2005/2006', '2005/2006'), ('2006/2007', '2006/2007'), ('2007/2008', '2007/2008'), ('2008/2009', '2008/2009'), ('2009/2010', '2009/2010'), ('2010/2011', '2010/2011'), ('2011/2012', '2011/2012'), ('2012/2013', '2012/2013'), ('2013/2014', '2013/2014'), ('2014/2015', '2014/2015'), ('2015/2016', '2015/2016'), ('2016/2017', '2016/2017'), ('2017/2018', '2017/2018'), ('2018/2019', '2018/2019'), ('2019/2020', '2019/2020'), ('2020/2021', '2020/2021'), ('2021/2022', '2021/2022'), ('2022/2023', '2022/2023')], max_length=255, verbose_name='Session'),
        ),
        migrations.AlterField(
            model_name='executive_okija',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_okija', to='account.profile_okija'),
        ),
        migrations.AlterField(
            model_name='executive_okija',
            name='session',
            field=models.CharField(blank=True, choices=[('1999/2000', '1999/2000'), ('2000/2001', '2000/2001'), ('2001/2002', '2001/2002'), ('2002/2003', '2002/2003'), ('2003/2004', '2003/2004'), ('2004/2005', '2004/2005'), ('2005/2006', '2005/2006'), ('2006/2007', '2006/2007'), ('2007/2008', '2007/2008'), ('2008/2009', '2008/2009'), ('2009/2010', '2009/2010'), ('2010/2011', '2010/2011'), ('2011/2012', '2011/2012'), ('2012/2013', '2012/2013'), ('2013/2014', '2013/2014'), ('2014/2015', '2014/2015'), ('2015/2016', '2015/2016'), ('2016/2017', '2016/2017'), ('2017/2018', '2017/2018'), ('2018/2019', '2018/2019'), ('2019/2020', '2019/2020'), ('2020/2021', '2020/2021'), ('2021/2022', '2021/2022'), ('2022/2023', '2022/2023')], max_length=255, verbose_name='Session'),
        ),
        migrations.AlterField(
            model_name='position_akpugo',
            name='campus',
            field=models.CharField(default='Akpugo', editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='position_akpugo',
            name='pos',
            field=models.CharField(help_text='Enter the position in full', max_length=255, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='position_elele',
            name='campus',
            field=models.CharField(default='Elele', editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='position_elele',
            name='pos',
            field=models.CharField(help_text='Enter the position in full', max_length=255, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='position_national',
            name='campus',
            field=models.CharField(default='National', editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='position_national',
            name='pos',
            field=models.CharField(help_text='Enter the position in full', max_length=255, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='position_okija',
            name='campus',
            field=models.CharField(default='Okija', editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='position_okija',
            name='pos',
            field=models.CharField(help_text='Enter the position in full', max_length=255, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='profile_akpugo',
            name='campus',
            field=models.CharField(choices=[('Akpugo', 'Akpugo'), ('None', 'None')], default='Akpugo', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile_akpugo',
            name='department',
            field=models.CharField(default='none', max_length=255, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='profile_akpugo',
            name='firstname',
            field=models.CharField(max_length=255, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profile_akpugo',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=255, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='profile_akpugo',
            name='lastname',
            field=models.CharField(max_length=255, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='profile_akpugo',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Religious', 'Religious')], max_length=255, verbose_name='Marital Status'),
        ),
        migrations.AlterField(
            model_name='profile_akpugo',
            name='phone_num',
            field=models.CharField(blank=True, max_length=255, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='profile_akpugo',
            name='state',
            field=models.CharField(blank=True, choices=[('Abia State', 'Abia State'), ('Adamawa State', 'Adamawa State'), ('Akwa Ibom State', 'Akwa Ibom State'), ('Anambra State', 'Anambra State'), ('Bauchi State', 'Bauchi State'), ('Bayelsa State', 'Bayelsa State'), ('Benue State', 'Benue State'), ('Borno State', 'Borno State'), ('Cross River State', 'Cross River State'), ('Delta State', 'Delta State'), ('Ebonyi State', 'Ebonyi State'), ('Edo State', 'Edo State'), ('Ekiti State', 'Ekiti State'), ('Enugu State', 'Enugu State'), ('Gombe State', 'Gombe State'), ('Imo State', 'Imo State'), ('Jigawa State', 'Jigawa State'), ('Kaduna State', 'Kaduna State'), ('Kano State', 'Kano State'), ('Kebbi State', 'Kebbi State'), ('Kogi State', 'Kogi State'), ('Kwara State', 'Kwara State'), ('Lagos State', 'Lagos State'), ('Nasarawa State', 'Nasarawa State'), ('Niger State', 'Niger State'), ('Ogun State', 'Ogun State'), ('Ondo State', 'Ondo State'), ('Osun State', 'Osun State'), ('Oyo State', 'Oyo State'), ('Plateau State', 'Plateau State'), ('Rivers State', 'Rivers State'), ('Sokoto State', 'Sokoto State'), ('Taraba State', 'Taraba State'), ('Yobe State', 'Yobe State'), ('Zamfara State', 'Zamfara State')], max_length=255, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='profile_elele',
            name='campus',
            field=models.CharField(choices=[('Elele', 'Elele'), ('None', 'None')], default='Elele', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile_elele',
            name='department',
            field=models.CharField(default='none', max_length=255, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='profile_elele',
            name='firstname',
            field=models.CharField(max_length=255, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profile_elele',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=255, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='profile_elele',
            name='lastname',
            field=models.CharField(max_length=255, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='profile_elele',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Religious', 'Religious')], max_length=255, verbose_name='Marital Status'),
        ),
        migrations.AlterField(
            model_name='profile_elele',
            name='phone_num',
            field=models.CharField(blank=True, max_length=255, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='profile_elele',
            name='state',
            field=models.CharField(blank=True, choices=[('Abia State', 'Abia State'), ('Adamawa State', 'Adamawa State'), ('Akwa Ibom State', 'Akwa Ibom State'), ('Anambra State', 'Anambra State'), ('Bauchi State', 'Bauchi State'), ('Bayelsa State', 'Bayelsa State'), ('Benue State', 'Benue State'), ('Borno State', 'Borno State'), ('Cross River State', 'Cross River State'), ('Delta State', 'Delta State'), ('Ebonyi State', 'Ebonyi State'), ('Edo State', 'Edo State'), ('Ekiti State', 'Ekiti State'), ('Enugu State', 'Enugu State'), ('Gombe State', 'Gombe State'), ('Imo State', 'Imo State'), ('Jigawa State', 'Jigawa State'), ('Kaduna State', 'Kaduna State'), ('Kano State', 'Kano State'), ('Kebbi State', 'Kebbi State'), ('Kogi State', 'Kogi State'), ('Kwara State', 'Kwara State'), ('Lagos State', 'Lagos State'), ('Nasarawa State', 'Nasarawa State'), ('Niger State', 'Niger State'), ('Ogun State', 'Ogun State'), ('Ondo State', 'Ondo State'), ('Osun State', 'Osun State'), ('Oyo State', 'Oyo State'), ('Plateau State', 'Plateau State'), ('Rivers State', 'Rivers State'), ('Sokoto State', 'Sokoto State'), ('Taraba State', 'Taraba State'), ('Yobe State', 'Yobe State'), ('Zamfara State', 'Zamfara State')], max_length=255, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='profile_national',
            name='campus',
            field=models.CharField(choices=[('National', 'National'), ('None', 'None')], default='National', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile_national',
            name='department',
            field=models.CharField(default='none', max_length=255, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='profile_national',
            name='firstname',
            field=models.CharField(max_length=255, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profile_national',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=255, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='profile_national',
            name='lastname',
            field=models.CharField(max_length=255, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='profile_national',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Religious', 'Religious')], max_length=255, verbose_name='Marital Status'),
        ),
        migrations.AlterField(
            model_name='profile_national',
            name='phone_num',
            field=models.CharField(blank=True, max_length=255, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='profile_national',
            name='state',
            field=models.CharField(blank=True, choices=[('Abia State', 'Abia State'), ('Adamawa State', 'Adamawa State'), ('Akwa Ibom State', 'Akwa Ibom State'), ('Anambra State', 'Anambra State'), ('Bauchi State', 'Bauchi State'), ('Bayelsa State', 'Bayelsa State'), ('Benue State', 'Benue State'), ('Borno State', 'Borno State'), ('Cross River State', 'Cross River State'), ('Delta State', 'Delta State'), ('Ebonyi State', 'Ebonyi State'), ('Edo State', 'Edo State'), ('Ekiti State', 'Ekiti State'), ('Enugu State', 'Enugu State'), ('Gombe State', 'Gombe State'), ('Imo State', 'Imo State'), ('Jigawa State', 'Jigawa State'), ('Kaduna State', 'Kaduna State'), ('Kano State', 'Kano State'), ('Kebbi State', 'Kebbi State'), ('Kogi State', 'Kogi State'), ('Kwara State', 'Kwara State'), ('Lagos State', 'Lagos State'), ('Nasarawa State', 'Nasarawa State'), ('Niger State', 'Niger State'), ('Ogun State', 'Ogun State'), ('Ondo State', 'Ondo State'), ('Osun State', 'Osun State'), ('Oyo State', 'Oyo State'), ('Plateau State', 'Plateau State'), ('Rivers State', 'Rivers State'), ('Sokoto State', 'Sokoto State'), ('Taraba State', 'Taraba State'), ('Yobe State', 'Yobe State'), ('Zamfara State', 'Zamfara State')], max_length=255, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='profile_okija',
            name='campus',
            field=models.CharField(choices=[('Okija', 'Okija'), ('None', 'None')], default='Okija', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile_okija',
            name='department',
            field=models.CharField(default='none', max_length=255, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='profile_okija',
            name='firstname',
            field=models.CharField(max_length=255, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profile_okija',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=255, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='profile_okija',
            name='lastname',
            field=models.CharField(max_length=255, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='profile_okija',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Religious', 'Religious')], max_length=255, verbose_name='Marital Status'),
        ),
        migrations.AlterField(
            model_name='profile_okija',
            name='phone_num',
            field=models.CharField(blank=True, max_length=255, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='profile_okija',
            name='state',
            field=models.CharField(blank=True, choices=[('Abia State', 'Abia State'), ('Adamawa State', 'Adamawa State'), ('Akwa Ibom State', 'Akwa Ibom State'), ('Anambra State', 'Anambra State'), ('Bauchi State', 'Bauchi State'), ('Bayelsa State', 'Bayelsa State'), ('Benue State', 'Benue State'), ('Borno State', 'Borno State'), ('Cross River State', 'Cross River State'), ('Delta State', 'Delta State'), ('Ebonyi State', 'Ebonyi State'), ('Edo State', 'Edo State'), ('Ekiti State', 'Ekiti State'), ('Enugu State', 'Enugu State'), ('Gombe State', 'Gombe State'), ('Imo State', 'Imo State'), ('Jigawa State', 'Jigawa State'), ('Kaduna State', 'Kaduna State'), ('Kano State', 'Kano State'), ('Kebbi State', 'Kebbi State'), ('Kogi State', 'Kogi State'), ('Kwara State', 'Kwara State'), ('Lagos State', 'Lagos State'), ('Nasarawa State', 'Nasarawa State'), ('Niger State', 'Niger State'), ('Ogun State', 'Ogun State'), ('Ondo State', 'Ondo State'), ('Osun State', 'Osun State'), ('Oyo State', 'Oyo State'), ('Plateau State', 'Plateau State'), ('Rivers State', 'Rivers State'), ('Sokoto State', 'Sokoto State'), ('Taraba State', 'Taraba State'), ('Yobe State', 'Yobe State'), ('Zamfara State', 'Zamfara State')], max_length=255, verbose_name='State'),
        ),
    ]
