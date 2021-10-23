import pymysql, os, json
from database.database import db

# read JSON file which is in the next parent folder
#file = os.path.abspath('../../..') + "/test.json"
file = os.path.abspath("home/JSON/DWI/JSONDWI.json")

json_data=open(file).read()
json_obj = json.loads(json_data)


# do validation and checks before insert
def validate_string(val):
   if val != None:
        if type(val) is int:
            #for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val


# connect to MySQL

cursor = db.cursor()


# parse json data to SQL insert
for i, item in enumerate(json_obj):
    #print(validate_string(item['eor_dtl'][0]['dmg_loc']))
    DWINO = validate_string(item.get("DWINO", None))
    DWIDATE = validate_string(item.get("DWIDATE", None))
    DWISTATUS = validate_string(item.get("DWISTATUS", None))
    EXPIREDDATETIME = validate_string(item.get("EXPIREDDATETIME", None))
    DEPOTID = validate_string(item.get("DEPOTID", None))
    REFTYPE = validate_string(item.get("REFTYPE", None))
    REFNO = validate_string(item.get("REFNO", None))
    INSTRUCTCODE = validate_string(item.get("INSTRUCTCODE", None))
    CONTAINERNO = validate_string(item.get("CONTAINERNO", None))
    CONTSZ = validate_string(item.get("CONTSZ", None))
    CONTTP = validate_string(item.get("CONTTP", None))
    QTY = validate_string(item.get("QTY", None))
    FE = validate_string(item.get("FE", None))
    FG = validate_string(item.get("FG", None))
    DG = validate_string(item.get("DG", None))
    CONTPRINCIPAL = validate_string(item.get("CONTPRINCIPAL", None))
    CONTOWNER = validate_string(item.get("CONTOWNER", None))
    CUSTCODE = validate_string(item.get("CUSTCODE", None))
    CUSTNAME = validate_string(item.get("CUSTNAME", None))
    VESSEL = validate_string(item.get("VESSEL", None))
    VOYAGE = validate_string(item.get("VOYAGE", None))
    POL = validate_string(item.get("POL", None))
    POT = validate_string(item.get("POT", None))
    POD = validate_string(item.get("POD", None))
    REMARK = validate_string(item.get("REMARK", None))
    INPUTTEDBY = validate_string(item.get("INPUTTEDBY", None))
    INPUTTEDON = validate_string(item.get("INPUTTEDON", None))
    REASON = validate_string(item.get("REASON", None))
    SEALNO = validate_string(item.get("SEALNO", None))
    SEALNO1 = validate_string(item.get("SEALNO1", None))
    SEALNO2 = validate_string(item.get("SEALNO2", None))
    WEIGHT = validate_string(item.get("WEIGHT", None))
    CMDTY = validate_string(item.get("CMDTY", None))
    DWIREQREF = validate_string(item.get("DWIREQREF", None))
    BKGNO = validate_string(item.get("BKGNO", None))
    MLO_CLEANING = validate_string(item.get("MLO_CLEANING", None))
    BILL_TO_PARTY = validate_string(item.get("BILL_TO_PARTY", None))
    NPWP = validate_string(item.get("NPWP", None))
    NOPOL = validate_string(item.get("NOPOL", None))
    DRIVER_NAME = validate_string(item.get("DRIVER_NAME", None))
    DISCHARGE_DATE = validate_string(item.get("DISCHARGE_DATE", None))
    CY_GATEOUT_DATE = validate_string(item.get("CY_GATEOUT_DATE", None))
    LOAD_DATE = validate_string(item.get("LOAD_DATE", None))
    SP2 = validate_string(item.get("SP2", None))
    DMG = validate_string(item.get("DMG", None))
    
    cursor.execute("""INSERT INTO importjsondwisql  
    (DWINO, DWIDATE, DWISTATUS, EXPIREDDATETIME, DEPOTID,REFTYPE, REFNO,INSTRUCTCODE, 
    CONTAINERNO, CONTSZ,CONTTP, QTY, FE, FG, DG, CONTPRINCIPAL, 
    CONTOWNER,CUSTCODE, CUSTNAME, VESSEL, VOYAGE, POL, POT, POD, 
    REMARK, INPUTTEDBY, INPUTTEDON,REASON, SEALNO,SEALNO1, SEALNO2, WEIGHT, 
    CMDTY, DWIREQREF, BKGNO, MLO_CLEANING,BILL_TO_PARTY, NPWP, NOPOL, DRIVER_NAME, 
    DISCHARGE_DATE, CY_GATEOUT_DATE, LOAD_DATE, SP2, DMG) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", 
    (DWINO, DWIDATE, DWISTATUS, EXPIREDDATETIME, DEPOTID,REFTYPE, REFNO,INSTRUCTCODE, 
    CONTAINERNO, CONTSZ,CONTTP, QTY, FE, FG, 
    DG, CONTPRINCIPAL, CONTOWNER,CUSTCODE, CUSTNAME, VESSEL, 
    VOYAGE, POL, POT, POD, REMARK, INPUTTEDBY, INPUTTEDON,
    REASON, SEALNO,SEALNO1, SEALNO2, WEIGHT, CMDTY, 
    DWIREQREF, BKGNO, MLO_CLEANING,BILL_TO_PARTY, NPWP, NOPOL, 
    DRIVER_NAME, DISCHARGE_DATE, CY_GATEOUT_DATE, LOAD_DATE, SP2, DMG))

db.commit()
db.close()