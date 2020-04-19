# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Migrationhistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', primary_key=True, max_length=150)  # Field name made lowercase.
    contextkey = models.CharField(db_column='ContextKey', max_length=300)  # Field name made lowercase.
    model = models.TextField(db_column='Model')  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '__migrationhistory'


class Appclients(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=128, blank=True, null=True)  # Field name made lowercase.
    apptypeid = models.ForeignKey('Apptypes', models.DO_NOTHING, db_column='AppTypeId')  # Field name made lowercase.
    recordkey = models.CharField(db_column='RecordKey', max_length=128, blank=True, null=True)  # Field name made lowercase.
    recordcreated = models.DateTimeField(db_column='RecordCreated', blank=True, null=True)  # Field name made lowercase.
    recordmodified = models.DateTimeField(db_column='RecordModified', blank=True, null=True)  # Field name made lowercase.
    recorddeleted = models.IntegerField(db_column='RecordDeleted')  # Field name made lowercase.
    clientid = models.CharField(db_column='ClientId', max_length=128, blank=True, null=True)  # Field name made lowercase.
    clientsecret = models.CharField(db_column='ClientSecret', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isinactive = models.IntegerField(db_column='IsInactive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'appclients'


class Apptypes(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=128, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=128, blank=True, null=True)  # Field name made lowercase.
    recordkey = models.CharField(db_column='RecordKey', max_length=128, blank=True, null=True)  # Field name made lowercase.
    recordcreated = models.DateTimeField(db_column='RecordCreated', blank=True, null=True)  # Field name made lowercase.
    recordmodified = models.DateTimeField(db_column='RecordModified', blank=True, null=True)  # Field name made lowercase.
    recorddeleted = models.IntegerField(db_column='RecordDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'apptypes'


class Aviusers(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=128)  # Field name made lowercase.
    firstname = models.CharField(db_column='Firstname', max_length=128)  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=128)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=128)  # Field name made lowercase.
    passwordhashed = models.CharField(db_column='PasswordHashed', max_length=128, blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=3, blank=True, null=True)  # Field name made lowercase.
    recordkey = models.CharField(db_column='RecordKey', max_length=128, blank=True, null=True)  # Field name made lowercase.
    recordcreated = models.DateTimeField(db_column='RecordCreated', blank=True, null=True)  # Field name made lowercase.
    recordmodified = models.DateTimeField(db_column='RecordModified', blank=True, null=True)  # Field name made lowercase.
    recorddeleted = models.IntegerField(db_column='RecordDeleted')  # Field name made lowercase.
    authorizedapps = models.IntegerField(db_column='AuthorizedApps')  # Field name made lowercase.
    isazureadenabled = models.IntegerField(db_column='IsAzureADEnabled')  # Field name made lowercase.
    azurename = models.TextField(db_column='AzureName', blank=True, null=True)  # Field name made lowercase.
    azuresubject = models.TextField(db_column='AzureSubject', blank=True, null=True)  # Field name made lowercase.
    azureusername = models.TextField(db_column='AzureUsername', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aviusers'


class Billaccountbases(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    driverid = models.ForeignKey('Drivers', models.DO_NOTHING, db_column='DriverId', blank=True, null=True)  # Field name made lowercase.
    permitholderid = models.ForeignKey('Permitholders', models.DO_NOTHING, db_column='PermitHolderId', blank=True, null=True)  # Field name made lowercase.
    discriminator = models.CharField(db_column='Discriminator', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'billaccountbases'


class Billtransacts(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    billaccountid = models.ForeignKey(Billaccountbases, models.DO_NOTHING, db_column='BillAccountId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=2)  # Field name made lowercase.
    issued = models.DateTimeField(db_column='Issued')  # Field name made lowercase.
    transacttype = models.IntegerField(db_column='TransactType')  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    recordkey = models.CharField(db_column='RecordKey', max_length=128, blank=True, null=True)  # Field name made lowercase.
    recordcreated = models.DateTimeField(db_column='RecordCreated', blank=True, null=True)  # Field name made lowercase.
    recordmodified = models.DateTimeField(db_column='RecordModified', blank=True, null=True)  # Field name made lowercase.
    recorddeleted = models.IntegerField(db_column='RecordDeleted')  # Field name made lowercase.
    paymenttype = models.IntegerField(db_column='PaymentType', blank=True, null=True)  # Field name made lowercase.
    feetypeid = models.ForeignKey('Feetypes', models.DO_NOTHING, db_column='FeeTypeId')  # Field name made lowercase.
    feecomplexlog_code = models.CharField(db_column='FeeComplexLog_Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    feecomplexlog_title = models.CharField(db_column='FeeComplexLog_Title', max_length=256, blank=True, null=True)  # Field name made lowercase.
    feecomplexlog_fee = models.DecimalField(db_column='FeeComplexLog_Fee', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    feecomplexlog_financialcode = models.CharField(db_column='FeeComplexLog_FinancialCode', max_length=128, blank=True, null=True)  # Field name made lowercase.
    taxpst = models.DecimalField(db_column='TaxPST', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxhst = models.DecimalField(db_column='TaxHST', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'billtransacts'


class Cvodrivers(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    cvoid = models.ForeignKey('Permitholders', models.DO_NOTHING, db_column='CVOId')  # Field name made lowercase.
    driverid = models.ForeignKey('Drivers', models.DO_NOTHING, db_column='DriverId')  # Field name made lowercase.
    issued = models.DateTimeField(db_column='Issued')  # Field name made lowercase.
    expires = models.DateTimeField(db_column='Expires')  # Field name made lowercase.
    recordkey = models.CharField(db_column='RecordKey', max_length=128, blank=True, null=True)  # Field name made lowercase.
    recordcreated = models.DateTimeField(db_column='RecordCreated', blank=True, null=True)  # Field name made lowercase.
    recordmodified = models.DateTimeField(db_column='RecordModified', blank=True, null=True)  # Field name made lowercase.
    recorddeleted = models.IntegerField(db_column='RecordDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cvodrivers'


class Drivers(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    adcn = models.CharField(db_column='ADCN', max_length=50)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50)  # Field name made lowercase.
    passwordhashed = models.CharField(db_column='PasswordHashed', max_length=128, blank=True, null=True)  # Field name made lowercase.
    recordkey = models.CharField(db_column='RecordKey', max_length=128, blank=True, null=True)  # Field name made lowercase.
    recordcreated = models.DateTimeField(db_column='RecordCreated', blank=True, null=True)  # Field name made lowercase.
    recordmodified = models.DateTimeField(db_column='RecordModified', blank=True, null=True)  # Field name made lowercase.
    recorddeleted = models.IntegerField(db_column='RecordDeleted')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=128)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    messagemedia = models.IntegerField(db_column='MessageMedia')  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    photouri = models.TextField(db_column='PhotoUri', blank=True, null=True)  # Field name made lowercase.
    signatureuri = models.TextField(db_column='SignatureUri', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'drivers'


class Features(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=10)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=128)  # Field name made lowercase.
    colorcode = models.CharField(db_column='ColorCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    recordkey = models.CharField(db_column='RecordKey', max_length=128, blank=True, null=True)  # Field name made lowercase.
    recordcreated = models.DateTimeField(db_column='RecordCreated', blank=True, null=True)  # Field name made lowercase.
    recordmodified = models.DateTimeField(db_column='RecordModified', blank=True, null=True)  # Field name made lowercase.
    recorddeleted = models.IntegerField(db_column='RecordDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'features'


class Feetypes(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    feecomplex_code = models.CharField(db_column='FeeComplex_Code', max_length=50)  # Field name made lowercase.
    feecomplex_title = models.CharField(db_column='FeeComplex_Title', max_length=256)  # Field name made lowercase.
    feecomplex_fee = models.DecimalField(db_column='FeeComplex_Fee', max_digits=18, decimal_places=2)  # Field name made lowercase.
    feecomplex_financialcode = models.CharField(db_column='FeeComplex_FinancialCode', max_length=128)  # Field name made lowercase.
    isinactive = models.IntegerField(db_column='IsInactive')  # Field name made lowercase.
    recordkey = models.CharField(db_column='RecordKey', max_length=128, blank=True, null=True)  # Field name made lowercase.
    recordcreated = models.DateTimeField(db_column='RecordCreated', blank=True, null=True)  # Field name made lowercase.
    recordmodified = models.DateTimeField(db_column='RecordModified', blank=True, null=True)  # Field name made lowercase.
    recorddeleted = models.IntegerField(db_column='RecordDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'feetypes'


class Filerecords(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=128)  # Field name made lowercase.
    path = models.CharField(db_column='Path', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    contenttype = models.CharField(db_column='ContentType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    size = models.IntegerField(db_column='Size')  # Field name made lowercase.
    md5 = models.CharField(db_column='MD5', max_length=30, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    orderof = models.IntegerField(db_column='OrderOf')  # Field name made lowercase.
    recordkey = models.CharField(db_column='RecordKey', max_length=128, blank=True, null=True)  # Field name made lowercase.
    recordcreated = models.DateTimeField(db_column='RecordCreated', blank=True, null=True)  # Field name made lowercase.
    recordmodified = models.DateTimeField(db_column='RecordModified', blank=True, null=True)  # Field name made lowercase.
    recorddeleted = models.IntegerField(db_column='RecordDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'filerecords'


class Insurancepolicies(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    permitholderid = models.ForeignKey('Permitholders', models.DO_NOTHING, db_column='PermitHolderId')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.
    recordkey = models.CharField(db_column='RecordKey', max_length=128, blank=True, null=True)  # Field name made lowercase.
    recordcreated = models.DateTimeField(db_column='RecordCreated', blank=True, null=True)  # Field name made lowercase.
    recordmodified = models.DateTimeField(db_column='RecordModified', blank=True, null=True)  # Field name made lowercase.
    recorddeleted = models.IntegerField(db_column='RecordDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'insurancepolicies'


class Permitholders(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    accountnumber = models.CharField(db_column='AccountNumber', max_length=50)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=128, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=50, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    faxnumber = models.CharField(db_column='FaxNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=128, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=128)  # Field name made lowercase.
    recordkey = models.CharField(db_column='RecordKey', max_length=128, blank=True, null=True)  # Field name made lowercase.
    recordcreated = models.DateTimeField(db_column='RecordCreated', blank=True, null=True)  # Field name made lowercase.
    recordmodified = models.DateTimeField(db_column='RecordModified', blank=True, null=True)  # Field name made lowercase.
    recorddeleted = models.IntegerField(db_column='RecordDeleted')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    driverid = models.ForeignKey(Drivers, models.DO_NOTHING, db_column='DriverId', blank=True, null=True)  # Field name made lowercase.
    discriminator = models.CharField(db_column='Discriminator', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'permitholders'


class Permits(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    vehicleid = models.ForeignKey('Vehicles', models.DO_NOTHING, db_column='VehicleId')  # Field name made lowercase.
    permitholderid = models.ForeignKey(Permitholders, models.DO_NOTHING, db_column='PermitHolderId')  # Field name made lowercase.
    issued = models.DateTimeField(db_column='Issued')  # Field name made lowercase.
    expires = models.DateTimeField(db_column='Expires')  # Field name made lowercase.
    permittype = models.IntegerField(db_column='PermitType')  # Field name made lowercase.
    recordkey = models.CharField(db_column='RecordKey', max_length=128, blank=True, null=True)  # Field name made lowercase.
    recordcreated = models.DateTimeField(db_column='RecordCreated', blank=True, null=True)  # Field name made lowercase.
    recordmodified = models.DateTimeField(db_column='RecordModified', blank=True, null=True)  # Field name made lowercase.
    recorddeleted = models.IntegerField(db_column='RecordDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'permits'


class Recordchangelogs(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    recordkey = models.CharField(db_column='RecordKey', max_length=128, blank=True, null=True)  # Field name made lowercase.
    dateof = models.DateTimeField(db_column='DateOf')  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    action = models.IntegerField(db_column='Action')  # Field name made lowercase.
    recordtype = models.CharField(db_column='RecordType', max_length=128, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recordchangelogs'


class Rteventlogs(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    dateof = models.DateTimeField(db_column='DateOf')  # Field name made lowercase.
    level = models.IntegerField(db_column='Level')  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=256, blank=True, null=True)  # Field name made lowercase.
    message = models.TextField(db_column='Message', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rteventlogs'


class Vehicledrivers(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    vehicleid = models.ForeignKey('Vehicles', models.DO_NOTHING, db_column='VehicleId')  # Field name made lowercase.
    driverid = models.ForeignKey(Drivers, models.DO_NOTHING, db_column='DriverId')  # Field name made lowercase.
    issued = models.DateTimeField(db_column='Issued')  # Field name made lowercase.
    expires = models.DateTimeField(db_column='Expires')  # Field name made lowercase.
    recordkey = models.CharField(db_column='RecordKey', max_length=128, blank=True, null=True)  # Field name made lowercase.
    recordcreated = models.DateTimeField(db_column='RecordCreated', blank=True, null=True)  # Field name made lowercase.
    recordmodified = models.DateTimeField(db_column='RecordModified', blank=True, null=True)  # Field name made lowercase.
    recorddeleted = models.IntegerField(db_column='RecordDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehicledrivers'


class Vehiclefeatures(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    vehicleid = models.ForeignKey('Vehicles', models.DO_NOTHING, db_column='VehicleId')  # Field name made lowercase.
    featureid = models.ForeignKey(Features, models.DO_NOTHING, db_column='FeatureId')  # Field name made lowercase.
    recordkey = models.CharField(db_column='RecordKey', max_length=128, blank=True, null=True)  # Field name made lowercase.
    recordcreated = models.DateTimeField(db_column='RecordCreated', blank=True, null=True)  # Field name made lowercase.
    recordmodified = models.DateTimeField(db_column='RecordModified', blank=True, null=True)  # Field name made lowercase.
    recorddeleted = models.IntegerField(db_column='RecordDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehiclefeatures'


class Vehicleidentifiers(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    expired = models.DateTimeField(db_column='Expired')  # Field name made lowercase.
    inactive = models.IntegerField(db_column='Inactive')  # Field name made lowercase.
    issued = models.DateTimeField(db_column='Issued')  # Field name made lowercase.
    key = models.TextField(db_column='Key')  # Field name made lowercase.
    vehicleid = models.ForeignKey('Vehicles', models.DO_NOTHING, db_column='VehicleId')  # Field name made lowercase.
    recordkey = models.CharField(db_column='RecordKey', max_length=128, blank=True, null=True)  # Field name made lowercase.
    recordcreated = models.DateTimeField(db_column='RecordCreated', blank=True, null=True)  # Field name made lowercase.
    recordmodified = models.DateTimeField(db_column='RecordModified', blank=True, null=True)  # Field name made lowercase.
    recorddeleted = models.IntegerField(db_column='RecordDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehicleidentifiers'


class Vehicleinsurances(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    vehicleid = models.ForeignKey('Vehicles', models.DO_NOTHING, db_column='VehicleId')  # Field name made lowercase.
    issued = models.DateTimeField(db_column='Issued')  # Field name made lowercase.
    expires = models.DateTimeField(db_column='Expires')  # Field name made lowercase.
    recordkey = models.CharField(db_column='RecordKey', max_length=128, blank=True, null=True)  # Field name made lowercase.
    recordcreated = models.DateTimeField(db_column='RecordCreated', blank=True, null=True)  # Field name made lowercase.
    recordmodified = models.DateTimeField(db_column='RecordModified', blank=True, null=True)  # Field name made lowercase.
    recorddeleted = models.IntegerField(db_column='RecordDeleted')  # Field name made lowercase.
    policyid = models.ForeignKey(Insurancepolicies, models.DO_NOTHING, db_column='PolicyId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehicleinsurances'


class Vehicles(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    vehicletypeid = models.ForeignKey('Vehicletypes', models.DO_NOTHING, db_column='VehicleTypeId')  # Field name made lowercase.
    participatingtype = models.IntegerField(db_column='ParticipatingType')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=20)  # Field name made lowercase.
    deviceimei = models.CharField(db_column='DeviceIMEI', max_length=15)  # Field name made lowercase.
    recordkey = models.CharField(db_column='RecordKey', max_length=128, blank=True, null=True)  # Field name made lowercase.
    recordcreated = models.DateTimeField(db_column='RecordCreated', blank=True, null=True)  # Field name made lowercase.
    recordmodified = models.DateTimeField(db_column='RecordModified', blank=True, null=True)  # Field name made lowercase.
    recorddeleted = models.IntegerField(db_column='RecordDeleted')  # Field name made lowercase.
    make = models.CharField(db_column='Make', max_length=128, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=128, blank=True, null=True)  # Field name made lowercase.
    plate = models.CharField(db_column='Plate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=50, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=128, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    deviceserialnumber = models.CharField(db_column='DeviceSerialNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    avicategory = models.IntegerField(db_column='AVICategory', blank=True, null=True)  # Field name made lowercase.
    qrcode = models.CharField(db_column='QRCode', max_length=20)  # Field name made lowercase.
    ministryvin = models.CharField(db_column='MinistryVIN', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehicles'


class Vehicletypes(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=128)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=128)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=128, blank=True, null=True)  # Field name made lowercase.
    recordkey = models.CharField(db_column='RecordKey', max_length=128, blank=True, null=True)  # Field name made lowercase.
    recordcreated = models.DateTimeField(db_column='RecordCreated', blank=True, null=True)  # Field name made lowercase.
    recordmodified = models.DateTimeField(db_column='RecordModified', blank=True, null=True)  # Field name made lowercase.
    recorddeleted = models.IntegerField(db_column='RecordDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehicletypes'
