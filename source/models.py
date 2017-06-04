from django.db import models
from django.core.validators import RegexValidator


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'people'
        verbose_name_plural = 'people'

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Contract(models.Model):
    name = models.CharField(max_length=255)
    REVSHARE_TYPES = (
        ('gross', 'Gross'),
        ('net', 'Net'),
    )
    revshare_type = models.CharField(max_length=5, choices=REVSHARE_TYPES)
    kindle_inclusive_reveshare = models.DecimalField(max_digits=3, decimal_places=2)
    kindle_non_inclusive_reveshare = models.DecimalField(max_digits=4, decimal_places=3)
    apple_reveshare = models.DecimalField(max_digits=3, decimal_places=2)
    nook_reveshare = models.DecimalField(max_digits=3, decimal_places=2)
    google_reveshare = models.DecimalField(max_digits=3, decimal_places=2)
    smashwords_reveshare = models.DecimalField(max_digits=3, decimal_places=2)
    lightningsource_reveshare = models.DecimalField(max_digits=3, decimal_places=2)
    createspace_reveshare = models.DecimalField(max_digits=3, decimal_places=2)
    wholesale_reveshare = models.DecimalField(max_digits=3, decimal_places=2)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'contracts'

    def __str__(self):
        return self.name

class Title(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Person, db_table='x_authors_titles', related_name='authors')
    external_payee = models.BooleanField()
    payees = models.ManyToManyField(Person, db_table='x_payees_titles', related_name='payees')
    contract = models.ForeignKey(Contract)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'titles'

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.ForeignKey(Title)
    isbn = models.CharField(
        max_length = 13,
        validators = [
            RegexValidator(
                regex = r'^[\d]{13}$',
                message = 'The ISBN must be 13 digits.'
                )
            ]
        )
    asin = models.CharField(
        blank = True,
        max_length = 10,
        validators = [
            RegexValidator(
                regex = r'^B00([a-zA-Z0-9]{7})$',
                message = 'The ASIN must be 10 alphanumeric characters beginning with B00.'
            )
        ]
    )
    BOOK_TYPES = (
        ('ebook', 'eBook'),
        ('paperback', 'Paperback'),
        ('hardback', 'Hardback'),
    )
    book_type = models.CharField(max_length=9, choices=BOOK_TYPES)
    list_price = models.DecimalField(max_digits=4, decimal_places=2)
    adjustment = models.DecimalField(max_digits=4, decimal_places=2) # Adjustment type according to book type, where eBooks have a Google adjustment
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return '%s (%s)' % (self.title, self.book_type)

def upload_path(instance, filename):
# Uploads file to settings.MEDIA_ROOT/<filename>
    return filename

class File(models.Model):
    uploaded_file = models.FileField(upload_to=upload_path)
    FILE_TYPES = (
        ('kindle', 'Kindle'),
        ('apple', 'Apple'),
        ('nook', 'Nook'),
        ('google', 'Google'),
        ('smashwords', 'Smashwords'),
        ('lightningsource', 'Lightning Source'),
        ('createspace', 'CreateSpace'),
    )
    file_type = models.CharField(max_length=15, choices=FILE_TYPES)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'files'

    def __str__(self):
        return '%s (%s)' % (self.uploaded_file.name, self.file_type)

class Transaction(models.Model):
    book = models.ForeignKey(Book)
    transaction_date = models.DateField()
    revenue = models.DecimalField(max_digits=5, decimal_places=2)
    revshare = models.DecimalField(max_digits=5, decimal_places=2)
    gross_profit = models.DecimalField(max_digits=5, decimal_places=2)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'transactions'

    def __str__(self):
        return '%s (%s)' % (self.book.title, self.transaction_date)

class Currency(models.Model):
    CURRENCY_TYPES = (
        ('GBP', 'GBP'),
        ('EUR', 'EUR'),
        ('AUD', 'AUD'),
        ('JPY', 'JPY'),
        ('CAD', 'CAD'),
        ('NOK', 'NOK'),
        ('CHF', 'CHF'),
        ('SEK', 'SEK'),
        ('MXN', 'MXN'),
        ('NZD', 'NZD'),
        ('INR', 'INR'),
        ('BRL', 'BRL'),
        ('DKK', 'DKK'),
    )
    currency = models.CharField(max_length=3, choices=CURRENCY_TYPES)
    conversion_rate = models.DecimalField(max_digits=6, decimal_places=5)
    conversion_rate_date = models.DateField()
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'currencies'
        verbose_name_plural = 'currencies'

    def __str__(self):
        return '%s (%s)' % (self.currency, self.conversion_rate_date)
