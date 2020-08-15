# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Students(models.Model):
    number = models.CharField(db_column='Number', max_length=255)  # Field name made lowercase.
    geschl = models.CharField(db_column='Geschl', max_length=255)  # Field name made lowercase.
    hsprvli = models.CharField(db_column='HSprVLI', max_length=255)  # Field name made lowercase.
    hsprmli = models.CharField(db_column='HSprMLI', max_length=255)  # Field name made lowercase.
    hlvli = models.CharField(db_column='HLVLI', max_length=255)  # Field name made lowercase.
    hlmli = models.CharField(db_column='HLMLI', max_length=255)  # Field name made lowercase.
    hlkli = models.CharField(db_column='HLKLI', max_length=255)  # Field name made lowercase.
    multilingual = models.CharField(max_length=255)
    sprechs = models.CharField(db_column='SprechS', max_length=255)  # Field name made lowercase.
    less = models.CharField(db_column='LesS', max_length=255)  # Field name made lowercase.
    dazu = models.CharField(db_column='DaZU', max_length=255)  # Field name made lowercase.
    daza = models.CharField(db_column='DaZa', max_length=255)  # Field name made lowercase.
    mu_hsu = models.CharField(db_column='MU/HSU', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t1 = models.CharField(db_column='T1', max_length=255)  # Field name made lowercase.
    t2 = models.CharField(db_column='T2', max_length=255)  # Field name made lowercase.
    t3 = models.CharField(db_column='T3', max_length=255)  # Field name made lowercase.
    t4 = models.CharField(db_column='T4', max_length=255)  # Field name made lowercase.
    t5 = models.CharField(db_column='T5', max_length=255)  # Field name made lowercase.
    t6 = models.CharField(db_column='T6', max_length=255)  # Field name made lowercase.
    t7 = models.CharField(db_column='T7', max_length=255)  # Field name made lowercase.
    t8 = models.CharField(db_column='T8', max_length=255)  # Field name made lowercase.
    t9 = models.CharField(db_column='T9', max_length=255)  # Field name made lowercase.
    t10 = models.CharField(db_column='T10', max_length=255)  # Field name made lowercase.
    alt1 = models.FloatField(db_column='alt1')  # Field name made lowercase.
    alt10 = models.FloatField(db_column='alt10')  # Field name made lowercase.
    anzahl = models.IntegerField(db_column='Anzahl')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'students'


class Tbltokenbase(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    orig = models.CharField(max_length=255, blank=True, null=True)
    target = models.CharField(max_length=255, blank=True, null=True)
    erroneous = models.FloatField(blank=True, null=True)
    error_level = models.CharField(max_length=255, blank=True, null=True)
    text_id = models.CharField(max_length=255, blank=True, null=True)
    grade = models.FloatField(blank=True, null=True)
    pos = models.CharField(db_column='POS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phonemes = models.CharField(max_length=255, blank=True, null=True)
    phoneme_units = models.CharField(max_length=255, blank=True, null=True)
    no_phonemes = models.FloatField(blank=True, null=True)
    graphemes = models.CharField(max_length=255, blank=True, null=True)
    no_graphemes = models.FloatField(blank=True, null=True)
    syllable_units = models.CharField(max_length=255, blank=True, null=True)
    syllable_types = models.CharField(max_length=255, blank=True, null=True)
    no_syllables = models.FloatField(blank=True, null=True)
    morpheme_units = models.CharField(max_length=255, blank=True, null=True)
    morpheme_types = models.CharField(max_length=255, blank=True, null=True)
    no_morphemes = models.FloatField(blank=True, null=True)
    graph_comb = models.FloatField(blank=True, null=True)
    err_graph_comb = models.FloatField(blank=True, null=True)
    graph_marked = models.FloatField(blank=True, null=True)
    err_graph_marked = models.FloatField(blank=True, null=True)
    ie = models.FloatField(blank=True, null=True)
    err_ie = models.FloatField(blank=True, null=True)
    schwa_silent = models.FloatField(blank=True, null=True)
    err_schwa_silent = models.FloatField(blank=True, null=True)
    doublec_syl = models.FloatField(db_column='doubleC_syl', blank=True, null=True)  # Field name made lowercase.
    err_doublec_syl = models.FloatField(db_column='err_doubleC_syl', blank=True, null=True)  # Field name made lowercase.
    doublec_other = models.FloatField(db_column='doubleC_other', blank=True, null=True)  # Field name made lowercase.
    err_doublec_other = models.FloatField(db_column='err_doubleC_other', blank=True, null=True)  # Field name made lowercase.
    doublev = models.FloatField(db_column='doubleV', blank=True, null=True)  # Field name made lowercase.
    err_doublev = models.FloatField(db_column='err_doubleV', blank=True, null=True)  # Field name made lowercase.
    h_length = models.FloatField(blank=True, null=True)
    err_h_length = models.FloatField(blank=True, null=True)
    h_sep = models.FloatField(blank=True, null=True)
    err_h_sep = models.FloatField(blank=True, null=True)
    r_voc = models.FloatField(blank=True, null=True)
    err_r_voc = models.FloatField(blank=True, null=True)
    devoice_final = models.FloatField(blank=True, null=True)
    err_devoice_final = models.FloatField(blank=True, null=True)
    g_spirant = models.FloatField(blank=True, null=True)
    err_g_spirant = models.FloatField(blank=True, null=True)
    morph_bound = models.FloatField(blank=True, null=True)
    err_morph_bound = models.FloatField(blank=True, null=True)
    err_hyp = models.FloatField(blank=True, null=True)
    err_other = models.FloatField(blank=True, null=True)
    chl_type_abs = models.FloatField(blank=True, null=True)
    chl_type_norm = models.FloatField(blank=True, null=True)
    chl_bigram_sum = models.FloatField(blank=True, null=True)
    chl_bigram_min = models.FloatField(blank=True, null=True)
    chl_nein = models.FloatField(blank=True, null=True)
    chl_nei_old20 = models.FloatField(blank=True, null=True)
    chl_lemma = models.CharField(max_length=255, blank=True, null=True)
    chl_lemma_abs = models.FloatField(blank=True, null=True)
    chl_lemma_norm = models.FloatField(blank=True, null=True)
    type_zipf = models.FloatField(blank=True, null=True)
    lemma_zipf = models.FloatField(blank=True, null=True)
    story = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltokenbase'


class Tbltypebase(models.Model):
    target = models.CharField(max_length=255, blank=True, null=True)
    pos = models.CharField(db_column='POS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    no_tokens = models.FloatField(blank=True, null=True)
    no_spellings = models.FloatField(blank=True, null=True)
    perc_erroneous = models.FloatField(blank=True, null=True)
    no_texts = models.FloatField(blank=True, null=True)
    phonemes = models.CharField(max_length=255, blank=True, null=True)
    phoneme_units = models.CharField(max_length=255, blank=True, null=True)
    no_phonemes = models.FloatField(blank=True, null=True)
    graphemes = models.CharField(max_length=255, blank=True, null=True)
    no_graphemes = models.FloatField(blank=True, null=True)
    syllable_units = models.CharField(max_length=255, blank=True, null=True)
    syllable_types = models.CharField(max_length=255, blank=True, null=True)
    no_syllables = models.FloatField(blank=True, null=True)
    morpheme_units = models.CharField(max_length=255, blank=True, null=True)
    morpheme_types = models.CharField(max_length=255, blank=True, null=True)
    no_morphemes = models.FloatField(blank=True, null=True)
    graph_comb = models.FloatField(blank=True, null=True)
    graph_marked = models.FloatField(blank=True, null=True)
    ie = models.FloatField(blank=True, null=True)
    schwa_silent = models.FloatField(blank=True, null=True)
    doublec_syl = models.FloatField(db_column='doubleC_syl', blank=True, null=True)  # Field name made lowercase.
    doublec_other = models.FloatField(db_column='doubleC_other', blank=True, null=True)  # Field name made lowercase.
    doublev = models.FloatField(db_column='doubleV', blank=True, null=True)  # Field name made lowercase.
    h_length = models.FloatField(blank=True, null=True)
    h_sep = models.FloatField(blank=True, null=True)
    r_voc = models.FloatField(blank=True, null=True)
    devoice_final = models.FloatField(blank=True, null=True)
    g_spirant = models.FloatField(blank=True, null=True)
    morph_bound = models.FloatField(blank=True, null=True)
    chl_type_abs = models.FloatField(blank=True, null=True)
    chl_type_norm = models.FloatField(blank=True, null=True)
    chl_bigram_sum = models.FloatField(blank=True, null=True)
    chl_bigram_min = models.FloatField(blank=True, null=True)
    chl_nei_n = models.FloatField(blank=True, null=True)
    chl_nei_old20 = models.FloatField(blank=True, null=True)
    chl_lemma = models.CharField(max_length=255, blank=True, null=True)
    chl_lemma_abs = models.FloatField(blank=True, null=True)
    chl_lemma_norm = models.FloatField(blank=True, null=True)
    type_zipf = models.FloatField(blank=True, null=True)
    lemma_zipf = models.FloatField(blank=True, null=True)
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbltypebase'

