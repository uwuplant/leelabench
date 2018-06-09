from django.db.models import CharField, IntegerField, BooleanField
from django.db.models import FloatField, ForeignKey, DateTimeField
from django.db.models import PROTECT, Model

class LogEvent(Model):

    data     = CharField(max_length=256)
    creation = DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} : {1}".format(self.creation, self.data)

class Engine(Model):

    name    = CharField(max_length=128)
    source  = CharField(max_length=1024)
    proto   = CharField(max_length=16)
    sha     = CharField(max_length=64)
    bench   = IntegerField(default=0)

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.bench)

class Machine(Model):

    owner    = CharField(max_length=64)
    osname   = CharField(max_length=128)
    lastseen = DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}-{1} ({2})'.format(self.owner.name, self.osname, self.id)

class Results(Model):

    test     = ForeignKey('Test', PROTECT, related_name='test')
    machine  = ForeignKey('Machine', PROTECT, related_name='machine')

    games    = IntegerField(default=0)
    wins     = IntegerField(default=0)
    losses   = IntegerField(default=0)
    draws    = IntegerField(default=0)
    crashes  = IntegerField(default=0)
    time     = IntegerField(default=0)

    lastseen = DateTimeField(default=0)

    def __str__(self):
        return '{0} {1}'.format(self.test.dev.name, self.machine.__str__())

class Test(Model):

    dev         = ForeignKey('Engine', PROTECT, related_name='dev')
    base        = ForeignKey('Engine', PROTECT, related_name='base')

    devoptions  = CharField(max_length=256)
    baseoptions = CharField(max_length=256)

    bookname    = CharField(max_length=32)
    timecontrol = CharField(max_length=16)
    hashsize    = IntegerField(default=1)
    threads     = IntegerField(default=1)

    priority    = IntegerField(default=0)
    throughput  = IntegerField(default=0)

    alpha       = FloatField(default=0.0)
    beta        = FloatField(default=0.0)
    elolower    = FloatField(default=0.0)
    eloupper    = FloatField(default=0.0)

    lowerllr    = FloatField(default=0.0)
    currentllr  = FloatField(default=0.0)
    upperllr    = FloatField(default=0.0)

    elo         = FloatField(default=0.0)
    games       = IntegerField(default=0)
    wins        = IntegerField(default=0)
    draws       = IntegerField(default=0)
    losses      = IntegerField(default=0)

    passed      = BooleanField(default=False)
    failed      = BooleanField(default=False)
    deleted     = BooleanField(default=False)
    approved    = BooleanField(default=False)

    creation    = DateTimeField(auto_now=True)
    complted    = DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} vs {1} @ {2}'.format(self.dev.name, self.base.name, self.timecontrol)
