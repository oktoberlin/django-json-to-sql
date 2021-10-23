from django.db import models

class Importjsondwisql(models.Model):
    dwino = models.CharField(db_column='DWINO', max_length=50, primary_key=True)  # Field name made lowercase.
    dwidate = models.CharField(db_column='DWIDATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dwistatus = models.CharField(db_column='DWISTATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expireddatetime = models.CharField(db_column='EXPIREDDATETIME', max_length=50, blank=True, null=True)  # Field name made lowercase.    depotid = models.CharField(db_column='DEPOTID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reftype = models.CharField(db_column='REFTYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    refno = models.CharField(db_column='REFNO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    instructcode = models.CharField(db_column='INSTRUCTCODE', max_length=50, blank=True, null=True)  # Field name made lowercase.      
    containerno = models.CharField(db_column='CONTAINERNO', max_length=50, blank=True, null=True)  # Field name made lowercase.        
    contsz = models.CharField(db_column='CONTSZ', max_length=50, blank=True, null=True)  # Field name made lowercase.
    conttp = models.CharField(db_column='CONTTP', max_length=2, blank=True, null=True)  # Field name made lowercase.
    qty = models.CharField(db_column='QTY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fe = models.CharField(db_column='FE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fg = models.CharField(db_column='FG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dg = models.CharField(db_column='DG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    contprincipal = models.CharField(db_column='CONTPRINCIPAL', max_length=3, blank=True, null=True)  # Field name made lowercase.     
    contowner = models.CharField(db_column='CONTOWNER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    custcode = models.CharField(db_column='CUSTCODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    custname = models.CharField(db_column='CUSTNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vessel = models.CharField(db_column='VESSEL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    voyage = models.CharField(db_column='VOYAGE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pol = models.CharField(db_column='POL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pot = models.CharField(db_column='POT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pod = models.CharField(db_column='POD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inputtedby = models.CharField(db_column='INPUTTEDBY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inputtedon = models.CharField(db_column='INPUTTEDON', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(db_column='REASON', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sealno = models.CharField(db_column='SEALNO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sealno1 = models.CharField(db_column='SEALNO1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sealno2 = models.CharField(db_column='SEALNO2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    weight = models.CharField(db_column='WEIGHT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cmdty = models.CharField(db_column='CMDTY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dwireqref = models.CharField(db_column='DWIREQREF', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bkgno = models.CharField(db_column='BKGNO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mlo_cleaning = models.CharField(db_column='MLO_CLEANING', max_length=50, blank=True, null=True)  # Field name made lowercase.      
    bill_to_party = models.CharField(db_column='BILL_TO_PARTY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    npwp = models.CharField(db_column='NPWP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nopol = models.CharField(db_column='NOPOL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    driver_name = models.CharField(db_column='DRIVER_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.        
    vessel_name = models.CharField(db_column='VESSEL_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.        
    discharge_date = models.CharField(db_column='DISCHARGE_DATE', max_length=50, blank=True, null=True)  # Field name made lowercase.  
    cy_gateout_date = models.CharField(db_column='CY_GATEOUT_DATE', max_length=50, blank=True, null=True)  # Field name made lowercase.    load_date = models.CharField(db_column='LOAD_DATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sp2 = models.CharField(db_column='SP2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dmg = models.CharField(db_column='DMG', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'importjsondwisql'


class Importjsoneorsqld(models.Model):
    eorno = models.CharField(db_column='EORNO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dmg_loc = models.CharField(db_column='DMG_LOC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    component_code = models.CharField(db_column='COMPONENT_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.  
    repair_code = models.CharField(db_column='REPAIR_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.        
    dimension = models.IntegerField(db_column='DIMENSION', blank=True, null=True)  # Field name made lowercase.
    dimension_dtl = models.CharField(db_column='DIMENSION_DTL', max_length=50, blank=True, null=True)  # Field name made lowercase.    
    qty = models.CharField(db_column='QTY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    damage_code = models.CharField(db_column='DAMAGE_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.        
    damage_cause = models.CharField(db_column='DAMAGE_CAUSE', max_length=50, blank=True, null=True)  # Field name made lowercase.      
    currency = models.CharField(db_column='CURRENCY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    manhour = models.FloatField(db_column='MANHOUR', blank=True, null=True)  # Field name made lowercase.
    labour_cost = models.FloatField(db_column='LABOUR_COST', blank=True, null=True)  # Field name made lowercase.
    material_cost = models.FloatField(db_column='MATERIAL_COST', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CREATEDBY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdon = models.CharField(db_column='CREATEDON', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'importjsoneorsqld'


class Importjsoneorsqlh(models.Model):
    eorno = models.CharField(db_column='EORNO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dwino = models.CharField(db_column='DWINO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eordate = models.CharField(db_column='EORDATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    surveydate = models.CharField(db_column='SURVEYDATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    depotid = models.CharField(db_column='DEPOTID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    principal = models.CharField(db_column='PRINCIPAL', max_length=3, blank=True, null=True)  # Field name made lowercase.
    bookingno = models.CharField(db_column='BOOKINGNO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bl_do_no = models.CharField(db_column='BL_DO_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contno = models.CharField(db_column='CONTNO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contsize = models.CharField(db_column='CONTSIZE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    conttype = models.CharField(db_column='CONTTYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    contowner = models.CharField(db_column='CONTOWNER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contmfg = models.CharField(db_column='CONTMFG', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vessel = models.CharField(db_column='VESSEL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    voyage = models.CharField(db_column='VOYAGE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    custcode = models.CharField(db_column='CUSTCODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    custname = models.CharField(db_column='CUSTNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    surveyor = models.CharField(db_column='SURVEYOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    technician = models.CharField(db_column='TECHNICIAN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qc = models.CharField(db_column='QC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark_eor = models.CharField(db_column='REMARK_EOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eorstatus = models.CharField(db_column='EORSTATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    repairstatus = models.CharField(db_column='REPAIRSTATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.      
    createdby = models.CharField(db_column='CREATEDBY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdon = models.CharField(db_column='CREATEDON', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='VERSION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'importjsoneorsqlh'
