# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class Sword(models.Model):
    word = models.CharField(max_length=64, blank=True, null=True)
    meaning = models.CharField(max_length=128, blank=True, null=True)
    sentence_en = models.CharField(max_length=192, blank=True, null=True)
    sentence_ch = models.CharField(max_length=192, blank=True, null=True)

    def __str__(self):
        return "Sword({})".format(self.word)

    class Meta:
        db_table = 'sword'


class Vocabulary3500(models.Model):
    """高考3500"""
    word = models.CharField(max_length=64, blank=True, null=True)
    meaning = models.CharField(max_length=200, blank=True, null=True)
    sentence = models.CharField(max_length=255, blank=True, null=True)
    memory_method = models.CharField(max_length=200, blank=True, null=True)
    incorrect_times = models.IntegerField(blank=True, null=True)
    is_first_time = models.CharField(max_length=16, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'vocabulary3500'

    def __str__(self):
        return "Vocabulary3500({}  {}  {})".format(self.id, self.word, self.score)


class Vocabulary1575(models.Model):
    id = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=20, blank=True, null=True)
    meaning = models.CharField(max_length=200, blank=True, null=True)
    memory_method = models.CharField(max_length=200, blank=True, null=True)
    sentence = models.CharField(max_length=400, blank=True, null=True)
    incorrect_times = models.IntegerField(blank=True, null=True)
    word_type = models.ForeignKey('Vocabularytype', models.DO_NOTHING, blank=True, null=True)
    upronun = models.CharField(db_column='UPronun', max_length=80, blank=True, null=True)  # Field name made lowercase.
    upronun_url = models.CharField(db_column='UPronun_url', max_length=200, blank=True,
                                   null=True)  # Field name made lowercase.
    bpronun = models.CharField(db_column='BPronun', max_length=80, blank=True, null=True)  # Field name made lowercase.
    bpronun_url = models.CharField(db_column='BPronun_url', max_length=200, blank=True,
                                   null=True)  # Field name made lowercase.
    is_first_time = models.CharField(max_length=8, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'vocabulary1575'

    def __str__(self):
        return "Vocabulary1575({}  {}  {})".format(self.id, self.word, self.score)


class Vocabulary5500(models.Model):
    id = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=20, blank=True, null=True)
    meaning = models.CharField(max_length=200, blank=True, null=True)
    memory_method = models.CharField(max_length=200, blank=True, null=True)
    sentence = models.CharField(max_length=400, blank=True, null=True)
    incorrect_times = models.IntegerField(blank=True, null=True)
    word_type = models.ForeignKey('Vocabularytype', models.DO_NOTHING, blank=True, null=True)


    class Meta:
        db_table = 'vocabulary5500'


class Vocabularycet4(models.Model):
    id = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=20, blank=True, null=True)
    meaning = models.CharField(max_length=200, blank=True, null=True)
    memory_method = models.CharField(max_length=200, blank=True, null=True)
    sentence = models.CharField(max_length=400, blank=True, null=True)
    incorrect_times = models.IntegerField(blank=True, null=True)
    word_type = models.ForeignKey('Vocabularytype', models.DO_NOTHING, blank=True, null=True)
    upronun = models.CharField(db_column='UPronun', max_length=80, blank=True, null=True)  # Field name made lowercase.
    upronun_url = models.CharField(db_column='UPronun_url', max_length=200, blank=True,
                                   null=True)  # Field name made lowercase.
    bpronun = models.CharField(db_column='BPronun', max_length=80, blank=True, null=True)  # Field name made lowercase.
    bpronun_url = models.CharField(db_column='BPronun_url', max_length=200, blank=True,
                                   null=True)  # Field name made lowercase.

    is_first_time = models.CharField(max_length=16, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'vocabularycet4'

    def __str__(self):
        return "Vocabulary1575({}  {}  )".format(self.id, self.word)


class Vocabularycet6(models.Model):
    id = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=20, blank=True, null=True)
    meaning = models.CharField(max_length=200, blank=True, null=True)
    memory_method = models.CharField(max_length=200, blank=True, null=True)
    sentence = models.CharField(max_length=400, blank=True, null=True)
    incorrect_times = models.IntegerField(blank=True, null=True)
    word_type = models.ForeignKey('Vocabularytype', models.DO_NOTHING, blank=True, null=True)
    upronun = models.CharField(db_column='UPronun', max_length=80, blank=True, null=True)  # Field name made lowercase.
    upronun_url = models.CharField(db_column='UPronun_url', max_length=200, blank=True,
                                   null=True)  # Field name made lowercase.
    bpronun = models.CharField(db_column='BPronun', max_length=80, blank=True, null=True)  # Field name made lowercase.
    bpronun_url = models.CharField(db_column='BPronun_url', max_length=200, blank=True,
                                   null=True)  # Field name made lowercase.

    is_first_time = models.CharField(max_length=8, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'vocabularycet6'


class Vocabularytype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        db_table = 'vocabularytype'


class UserInfo(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    pwd = models.CharField(max_length=64, blank=True, null=True)
    wordtype = models.CharField(max_length=16, blank=True, null=True)
    wordposition = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'user_info'
