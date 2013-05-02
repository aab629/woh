from django.db import models

# Remember: models are classes, so they must be defined with capital letters
class Woh(models.Model):
    # Documentation on all field types (CharField, DateTimeField, etc.) can be found here:
    # https://docs.djangoproject.com/en/dev/ref/models/fields/
    trade_nm = models.CharField(max_length=255)
    street_addr_1_txt = models.CharField(max_length=255)
    cty_nm = models.CharField(max_length=255)
    st_cd = models.CharField(max_length=255)
    zip_cd = models.CharField(max_length=255)
    naics_code_description = models.CharField(max_length=255)
    case_violtn_cnt = models.IntegerField()
    ee_violtd_cnt = models.IntegerField()
    findings_start_date = models.DateTimeField()
    findings_end_date = models.DateTimeField()
    bw_atp_amt = models.DecimalField(max_digits=255, decimal_places=255)
    flsa_bw_atp_amt = models.DecimalField(max_digits=255, decimal_places=255)
    flsa_mw_bw_atp_amt = models.DecimalField(max_digits=255, decimal_places=255)
    flsa_ot_bw_atp_amt = models.DecimalField(max_digits=255, decimal_places=255)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    
    # We're using this to hook up to the crime_data table we already created
    class Meta:
        db_table = 'woh'

    # The __unicode__ method defines how an individual instance of this class
    # will represent itself as a string.
    def __unicode__(self):
        return self.trade_nm

