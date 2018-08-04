#Import the things
from struct import *
import sys
import math
#from IPython.core.debugger import Tracer
import pdb #; pdb.set_trace()
#%debug
#D://2360//Scripting_data//Python_trail//Stdffiles/20180607130537_CSC_NEG40C_001_S11E_N_T08-V93K_C2222B01SXX135P4.std
##class reader:
#Reading STDF file
#Input_file=Inputfile
#@staticmethod
def ReadFile(Inputfile):
    STDF_File=open(Inputfile,'rb')
    global STDF_Data
    STDF_Data=STDF_File.read()
#Creating the Dict for Records

All_Record_Names={}
All_Record_Names[0,10]=['FAR']
All_Record_Names[0,20]=['ATR']
All_Record_Names[0,30]=['VUR']
All_Record_Names[1,10]=['MIR']
All_Record_Names[1,20]=['MRR']
All_Record_Names[1,30]=['PCR']
All_Record_Names[1,40]=['HBR']
All_Record_Names[1,50]=['SBR']
All_Record_Names[1,60]=['PMR']
All_Record_Names[1,62]=['PGR']
All_Record_Names[1,63]=['PLR']
All_Record_Names[1,70]=['RDR']
All_Record_Names[1,80]=['SDR']
All_Record_Names[1,90]=['PSR']
All_Record_Names[1,91]=['NMR']
All_Record_Names[1,92]=['CNR']
All_Record_Names[1,93]=['SSR']
All_Record_Names[1,94]=['SCR']
All_Record_Names[2,10]=['WIR']
All_Record_Names[2,20]=['WRR']
All_Record_Names[2,30]=['WCR']
All_Record_Names[5,10]=['PIR']
All_Record_Names[5,20]=['PRR']
All_Record_Names[10,30]=['TSR']
All_Record_Names[15,10]=['PTR']
All_Record_Names[15,15]=['MPR']
All_Record_Names[15,20]=['FTR']
All_Record_Names[15,20]=['STR']
All_Record_Names[20,10]=['BPS']
All_Record_Names[20,20]=['EPS']
All_Record_Names[50,10]=['GDR']
All_Record_Names[50,30]=['DTR']
#Declaring some variables for further use age
global Starting_byte
#global Next_Reading_Byte,Record_lenght,Record_Name,End_Record_Byte,Number_Of_Sites,Record_name
Next_Reading_Byte=0
Starting_byte=0

Record_lenght=0
Record_Name='Null'
End_Record_Byte=0
Number_Of_Sites=0
Record_name="DontKnow"
#global Test_Details,Test_Flag_Details,TestNumbers,FullTestDetails,PartFullInfo
#global TestSummary_Report,Hbin_sumary,Sbin_sumary,PCR_Rec_Summary,GDR_Summary
Test_Details={'000':'TestNumber ,TestName ,LowLimit ,High Limit, Unit'}
Test_Flag_Details={'000':'OptFlag,TestResult Scaling Expo,Low Limit Scaling expo,High Limit Scaling expo,Low limit,High Lim,Test Unit,C Result Fmt String,C low lim fmt string,C High Lim Fmt string,Low spec,High Spec'}
TestNumbers=['Test Numbers']
FullTestDetails=['TestFull details']
PartFullInfo=[[['Part_Number'," "," "," "," "]],[['TestHeadNumber'," "," "," "," "]],[['SiteNumber'," "," "," "," "]],[['PartFlag'," "," "," "," "]],[['NumberofTestesExcicuted'," "," "," "," "]],[['HardBin'," "," "," "," "]],[['Softbin'," "," "," "," "]],[['X co'," "," "," "," "]],[['Y co'," "," "," "," "]]]
TestSummary_Report=[['Test Head number '],['Site number'],['Test type'],['test num'],['Exec cnt'],['Fail cnt'],['alaram cnt'],['test name'],['Seq name'],['Test lbl'],['opt flag'],
                    ['test tim'],['test min'],['test max'],['test sums'],['test sqares']]
Hbin_sumary=[['Head number'],['Site Number'],['Hbin Num'],['Hbin cnt'],['Hbin PF'],['Hbin name']]
Sbin_sumary=[['Head number'],['Site Number'],['Sbin Num'],['Sbin cnt'],['Sbin PF'],['Sbin name']]
PCR_Rec_Summary=[['Head number'],['Site Number'],['Part count'],['RTst_Cnt'],['Numb of abort during testing'],['Number of passed'],['Number of Functional']]
GDR_Summary=[]     

#Supporting functions

def Read_Variable_lenght_Char_Data(Starting_byte,Length_of_char):
    x,Starting_byte=One_Byte_Unsigned_int(Starting_byte,1)
    Byte_length_of_field=x[0]    
    if Byte_length_of_field>0:
        dumy=unpack( str(Byte_length_of_field) +'s',STDF_Data[Starting_byte:Starting_byte+Byte_length_of_field])
        return dumy, Starting_byte+Byte_length_of_field        
    elif Byte_length_of_field==0:
        Field='';return Field,Starting_byte+Byte_length_of_field;print('Field Empty :',Field)
def One_Byte_Unsigned_int(Starting_byte,Length_of_char): return unpack(str(Length_of_char)+'B',STDF_Data[Starting_byte:Starting_byte+Length_of_char]), Starting_byte+Length_of_char
def One_Byte_Signed_int(Starting_byte,Length_of_char):return unpack(str(Length_of_char)+'b',STDF_Data[Starting_byte:Starting_byte+Length_of_char]), Starting_byte+Length_of_char
def KX_One_Byte_Unsingned_int(Starting_byte,K_values):
    K=K_values[0];return unpack(str(K)+'B',STDF_Data[Starting_byte:Starting_byte+int(K)]), Starting_byte+int(K)
def Two_Byte_Unsigned_int(Starting_byte,Length_of_char): return unpack(str(Length_of_char)+'H',STDF_Data[Starting_byte:Starting_byte+(2*Length_of_char)]),Starting_byte+(2*Length_of_char)
def Two_Byte_Signed_int(Starting_byte,Length_of_char): return unpack(str(Length_of_char)+'h',STDF_Data[Starting_byte:Starting_byte+(2*Length_of_char)]), Starting_byte+(2*Length_of_char)
def Fourbyte_Floating_point(Starting_byte,Length_of_char): return unpack(str(Length_of_char)+'f',STDF_Data[Starting_byte:Starting_byte+(4*Length_of_char)]), Starting_byte+(4*Length_of_char)
def Four_Byte_Unsigned_int(Starting_byte,Length_of_char):return unpack(str(Length_of_char)+'I',STDF_Data[Starting_byte:Starting_byte+(4*Length_of_char)]), Starting_byte+(4*Length_of_char)
def Four_Byte_signed_int(Starting_byte,Length_of_char):return unpack(str(Length_of_char)+'i',STDF_Data[Starting_byte:Starting_byte+(4*Length_of_char)]), Starting_byte+(4*Length_of_char)
def Eightbyte_Floating_point(Starting_byte,Length_of_char): return unpack(str(Length_of_char)+'d',STDF_Data[Starting_byte:Starting_byte+(8*Length_of_char)]), Starting_byte+(8*Length_of_char)
def Fixed_lengh_Char(Starting_byte,Length_of_char):return unpack(str(Length_of_char)+'c',STDF_Data[Starting_byte:Starting_byte+Length_of_char]), Starting_byte+Length_of_char
def Fixed_Lenght_BitEncoded_data(Starting_byte,Bytelenght): return unpack(str(Bytelenght)+'s',STDF_Data[Starting_byte:Starting_byte+1]),Starting_byte+1
def Variable_len_BitencodedData(Starting_byte,Length_of_char):    
    x,Starting_byte=Two_Byte_Unsigned_int(Starting_byte,1)#;print(x[0])
    x=math.ceil(x[0]/8)
    if x>0:
        x,Starting_byte=One_Byte_Signed_int(Starting_byte,x);y=str(x[0]);x=' '.join(format(ord(i), 'b') for i in y)#print(y);x=format(ord(y),'b');lth=len(x)-1;x=x[lth:]#x=''.join(format(ord(i),'b') for i in y)#
        return x,Starting_byte  
    else:
        return x,Starting_byte
def Variable_len_BitEncoded_B(Starting_byte,Lenght_of_Char):    
    Nextbyte,Starting_byte=One_Byte_Unsigned_int(Starting_byte,1)
    #print(Starting_byte)
    if Nextbyte[0]>0:
        x,Starting_byte=One_Byte_Signed_int(Starting_byte, Nextbyte[0]);return x,Starting_byte
    elif Nextbyte[0]==0:
        return Nextbyte[0],Starting_byte
def __B0(Starting_byte):
    print('B0 not defined')


B0=__B0
U1=One_Byte_Unsigned_int
U2=Two_Byte_Unsigned_int
U4=Four_Byte_Unsigned_int
I1=One_Byte_Signed_int
I2=Two_Byte_Signed_int
I4=Four_Byte_signed_int
R4=Fourbyte_Floating_point
R8=Eightbyte_Floating_point
CN=Read_Variable_lenght_Char_Data
BN=Variable_len_BitEncoded_B
DN=Variable_len_BitencodedData
N1=KX_One_Byte_Unsingned_int
VN_MAP={'0':B0,'1':U1,'2':U2,'3':U4,'4':I1,'5':I2,'6':I4,'7':R4,'8':R8,'10':CN,'11':BN,'12':DN,'13':N1}

#Type record

def Record_header(Starting_byte):
    global End_Record_Byte,Record_name
    Rec_len,Starting_byte=U2(Starting_byte,1)
    Rec_type,Starting_byte=U1(Starting_byte,1)
    Rec_sub_type,Starting_byte=U1(Starting_byte,1)
    Record_name_key=Rec_type+Rec_sub_type
    End_Record_Byte=Starting_byte+Rec_len[0]   
    Record_name=All_Record_Names[Record_name_key]
    return Starting_byte;
    #;print('Record name :', Record_name)    
    #print("Record Length :",Rec_len[0])#;print('Stating record byte',Starting_byte)       

#Functions for getting the records & its data
def FAR(Starting_byte):
    CPU_TYPE,Starting_byte=U1(Starting_byte,1)
    STDF_VER,Starting_byte=U1(Starting_byte,1)
    print("CPU_type :",CPU_TYPE[0],"STDF_VER:",STDF_VER[0])#;Starting_byte+=1;
    return Starting_byte

def ATR(Starting_byte):
    MOD_TIM,Starting_byte=U4(Starting_byte,1)
    CMd_Line,Starting_byte=CN(Starting_byte,1)
    print("MOD_TIME :",MOD_TIM,"CMD_LINE :",CMd_Line)#;Starting_byte=CN(Starting_byte+4)
    return Starting_byte

def MIR(Starting_byte):
    if (Starting_byte<=End_Record_Byte): 
        Setuptime,Starting_byte=U4(Starting_byte,1)#;print('Setup time',Setuptime[0])
    else:
        print('Setup time',Setuptime)
    if (Starting_byte<=End_Record_Byte): 
        Strtuptime,Starting_byte=U4(Starting_byte,1)#;print('Start up time',Strtuptime[0])	
    else: 
        print('Start up time',Strtuptime)
    if (Starting_byte<=End_Record_Byte): 
        Stat_Num,Starting_byte=U1(Starting_byte,1)#;print('STAT NUM',Stat_Num[0])
    else: 
        print('STAT NUM',Stat_Num)
    if (Starting_byte<=End_Record_Byte): 
        print('MODE CODE',unpack('p',STDF_Data[Starting_byte:Starting_byte+1]));Starting_byte+=1
    else: 
        print('MODE CODE',"");Starting_byte+=1
    if (Starting_byte<=End_Record_Byte):
        print('RETEST CODE',unpack('p',STDF_Data[Starting_byte:Starting_byte+1]));Starting_byte+=1
    else: 
        print('RETEST CODE','');Starting_byte+=1
    if (Starting_byte<=End_Record_Byte): 
        print('PROT CODE',unpack('p',STDF_Data[Starting_byte:Starting_byte+1]));Starting_byte+=1
    else: 
        print('PROT CODE','');Starting_byte+=1
    if (Starting_byte<=End_Record_Byte): 
        Burntime,Starting_byte=U2(Starting_byte,1)#;print('BURN TIME',Burntime[0])	
    else:
        print('BURN TIME',Burntime);Starting_byte+=1
    if (Starting_byte<=End_Record_Byte): 
        print('CMOD_CODE',unpack('p',STDF_Data[Starting_byte:Starting_byte+1]));Starting_byte+=1
    else: 
        print('CMOD_CODE','Empty')
    if (Starting_byte<=End_Record_Byte): 
        Lotid,Starting_byte=CN(Starting_byte,1)#;print('LOT ID',Lotid[0])
    else: 
        print('LOT ID',"Empty") 
    if (Starting_byte<=End_Record_Byte): 
        Parttype,Starting_byte=CN(Starting_byte,1)#;print('PART_TYP',Parttype[0])
    else:  
        print('PART_TYP',"Empty")
    if (Starting_byte<=End_Record_Byte): 
        NodName,Starting_byte=CN(Starting_byte,1)#;print('NODE_NAM',NodName[0])
    else:
        print('NODE_NAM',"Empty")
    if (Starting_byte<=End_Record_Byte): 
        TesterType,Starting_byte=CN(Starting_byte,1)#;print('TESTER_TYPE',TesterType[0])
    else: 
        print('TESTER_TYPE',"Empty")
    if (Starting_byte<=End_Record_Byte):
        Jobname,Starting_byte=CN(Starting_byte,1)#;print('JOB_NAME',Jobname[0])
    else:
        print('LOT ID',"Empty")
    if (Starting_byte<=End_Record_Byte): 
        Jobrev,Starting_byte=CN(Starting_byte,1)#;print('JOB_REVISION',Jobrev[0])
    else: 
        print('JOB_NAME',"Empty")
    if (Starting_byte<=End_Record_Byte): 
        Sublotid,Starting_byte=CN(Starting_byte,1)#;print('SUBLOT_ID',Sublotid)
    else: 
        print('SUBLOT_ID',"Empty")
    if (Starting_byte<=End_Record_Byte): 
        Opername,Starting_byte=CN(Starting_byte,1)#;print('OPERATOR_NAME',Opername[0])
    else: 
        print('OPERATOR_NAME',"Empty")
    if (Starting_byte<=End_Record_Byte): 
        ExSwtype,Starting_byte=CN(Starting_byte,1)#;print('EXECUTIVE SW TYPE',ExSwtype[0])
    else: 
        print('EXECUTIVE SW TYPE',"Empty")
    if (Starting_byte<=End_Record_Byte):
        ExSwver,Starting_byte=CN(Starting_byte,1)#;print('EXECUTIVE SW VER NUM',ExSwver[0])
    else: 
        print('EXECUTIVE SW VER NUM',"Empty")
    if (Starting_byte<=End_Record_Byte):
        TestCode,Starting_byte=CN(Starting_byte,1)#;print('TEST CODE',TestCode)
    else: 
        print('TEST CODE',"Empty")
    if (Starting_byte<=End_Record_Byte): 
        TestTemp,Starting_byte=CN(Starting_byte,1)#;print('TEST TEMPRATURE',TestTemp)
    else:
        print('TEST TEMPRATURE',"Empty")
    if (Starting_byte<=End_Record_Byte): 
        GenUTest,Starting_byte=CN(Starting_byte,1)#;print('GENERIC USER TEXT',GenUTest)
    else: 
        print('GENERIC USER TEXT',"Empty")
    if (Starting_byte<=End_Record_Byte): 
        AuxDfile,Starting_byte=CN(Starting_byte,1)#;print('AUXILIARY DATA FILE',AuxDfile)
    else: 
        print('AUXILIARY DATA FILE',"Empty")
    if (Starting_byte<=End_Record_Byte): 
        Pcktyp,Starting_byte=CN(Starting_byte,1)#;print('PACKAGE TYPE',Pcktyp)
    else: 
        print('PACKAGE TYPE',"Empty")
    if (Starting_byte<=End_Record_Byte): 
        PFid,Starting_byte=CN(Starting_byte,1)#;print('PRODUCT FAMILY ID',PFid) 
    else: 
        print('PRODUCT FAMILY ID',"Empty")
    if (Starting_byte<=End_Record_Byte): 
        DataCode,Starting_byte=CN(Starting_byte,1)#;print('DATE CODE',DataCode)
    else: 
        print('DATE CODE',"Empty")
    if (Starting_byte<=End_Record_Byte): 
        FacilId,Starting_byte=CN(Starting_byte,1)#;print('FACIL_ID',FacilId) 
    else:
        print('FACIL_ID',"Empty")
    if (Starting_byte<=End_Record_Byte): 
        FloriId,Starting_byte=CN(Starting_byte,1)#;print('FLOOR_ID',FloriId)	
    else: 
        print('FLOOR_ID',"Empty")
    if (Starting_byte<=End_Record_Byte):
        FabPId,Starting_byte=CN(Starting_byte,1)#;print('FAB_PROCESS_ID',FabPId)
    else: 
        print('LOT ID',"Empty")
    if (Starting_byte<=End_Record_Byte):
        OpFreq,Starting_byte=CN(Starting_byte,1)#;print('OPERATION FREQ',OpFreq)  
    else:  
        print('OPERATION FREQ',"Empty")
    if (Starting_byte<=End_Record_Byte):
        TestSpecVerName,Starting_byte=CN(Starting_byte,1)#;print('TEST SPEC VER NAME',TestSpecVerName) 
    else:
        print('TEST SPEC VER NAME',"Empty")
    if (Starting_byte<=End_Record_Byte): 
        FlowId,Starting_byte=CN(Starting_byte,1)#;print('FLOW ID',FlowId) 
    else: 
        print('FLOW ID',"Empty")
    if (Starting_byte<=End_Record_Byte):
        SetupId,Starting_byte=CN(Starting_byte,1)#;print('SETUP ID',SetupId)  
    else: 
        print('SETUP ID',"Empty")
    if (Starting_byte<=End_Record_Byte):
        DDrev,Starting_byte=CN(Starting_byte,1)#;print('DEVICE DESIGN REVI',DDrev) 
    else: 
        print('DEVICE DESIGN REVI',"Empty")
    if (Starting_byte<=End_Record_Byte):
        EnggId,Starting_byte=CN(Starting_byte,1)#;print('ENGG ID',EnggId) 
    else:
        Starting_byte=End_Record_Byte#;print('ENGG ID',"Empty")
    if (Starting_byte<=End_Record_Byte): 
        RomCode,Starting_byte=CN(Starting_byte,1)#;print('ROM CODE ID',RomCode)  
    else: 
        print('ROM CODE ID',"Empty");Starting_byte=End_Record_Byte;return Starting_byte 


def SDR(Starting_byte):    
    global Number_Of_Sites
    Testheadnumber,Starting_byte=U1(Starting_byte,1)##;print('Test Head number :',Testheadnumber[0])
    SiteGroup,Starting_byte=U1(Starting_byte,1)#;print('Site group :',SiteGroup[0])
    Number_Of_Sites=unpack('B',STDF_Data[Starting_byte:Starting_byte+1])
    NumberofSites,Starting_byte=U1(Starting_byte,1)#;print('Number of sites :',NumberofSites[0])
    SiteNumber,Starting_byte=N1(Starting_byte,Number_Of_Sites)#;print("site_numbers :",SiteNumber)
    Handlertype,Starting_byte=CN(Starting_byte,1)#;print("Handler type / Prober Type :",Handlertype)
    HandlerId,Starting_byte=CN(Starting_byte,1)#;print("Handler ID / Prober ID :",HandlerId )
    CardType,Starting_byte=CN(Starting_byte,1)#;print("Card Type :",CardType)
    CardId,Starting_byte=CN(Starting_byte,1)#;print("Card ID :",CardId )
    LoadBrdType,Starting_byte=CN(Starting_byte,1)#;print("Load Board Type :",LoadBrdType)
    LoadBrdId,Starting_byte=CN(Starting_byte,1)#;print("Load Board ID:",LoadBrdId )
    DibBrdTyp,Starting_byte=CN(Starting_byte,1)#;print("DIB Board Type :",DibBrdTyp)
    DibBrdId,Starting_byte=CN(Starting_byte,1)#;print("DIB Board ID :",DibBrdId)
    Intefctyp,Starting_byte=CN(Starting_byte,1)#;print("Interface Cable Type :",Intefctyp)
    InterfaceId,Starting_byte=CN(Starting_byte,1); print("Interface Cable ID :",InterfaceId)
    HandlerContType,Starting_byte=CN(Starting_byte,1)#;print("Handler Contacter Type :",HandlerContType)
    HandlerContId,Starting_byte=CN(Starting_byte,1)#;print("Handler contacter ID :",HandlerContId)
    LaserType,Starting_byte=CN(Starting_byte,1)#;print("Laser Type :",LaserType)
    LaserId,Starting_byte=CN(Starting_byte,1)#;print("Laser ID :",LaserId)
    ExtraEQtype,Starting_byte=CN(Starting_byte,1)#;print("Extra Equipment Type :",ExtraEQtype)
    ExtraEQId,Starting_byte=CN(Starting_byte,1)#;print("Extra Equipment ID :")
    return Starting_byte

def PMR(Starting_byte):    
    UIndex,Starting_byte=U2(Starting_byte,1)#;print('Unique index associated with pin :',UIndex[0])
    ChanelType,Starting_byte=U2(Starting_byte,1)#;print('Channel Type :',ChanelType[0])
    ChanelName,Starting_byte=CN(Starting_byte,1)#;print('Channel Name :',ChanelName )
    PhNameOfPin,Starting_byte=CN(Starting_byte,1)#;print('Physical Name of Pin :',PhNameOfPin )
    LocalNameofPin,Starting_byte=CN(Starting_byte,1)#;print('Local name of Pin :',LocalNameofPin)
    HeadNumber,Starting_byte=U1(Starting_byte,1)#;print('Head number :',HeadNumber[0])
    SiteNumber,Starting_byte=U1(Starting_byte,1)#;print('Site number :',SiteNumber[0]);
    return Starting_byte

def WCR(Starting_byte):    
    WaferSize,Starting_byte=R4(Starting_byte,1)#;print('Wafer Size :',WaferSize)
    DiHight,Starting_byte=R4(Starting_byte,1)#;print('Die Hight :',DiHight[0])
    DieWidht,Starting_byte=R4(Starting_byte,1)#;print('Die Width :',DieWidht[0])
    WaferUnits,Starting_byte=U1(Starting_byte,1)#;print('Wafer Units :',WaferUnits)
    Wflat,Starting_byte=Fixed_lengh_Char(Starting_byte,1)#;print('Orientation of wafer flat :',Wflat)
    X_Co,Starting_byte=I2(Starting_byte,1)#;print('X Coordinate of Center Die of Wafer :',X_Co[0])
    Y_Co,Starting_byte=I2(Starting_byte,1)#;print('Y Coordinate of Center Die of Wafer :',Y_Co[0])
    X_Co,Starting_byte=Fixed_lengh_Char(Starting_byte,1)#;print('Position of X direciton of Wafer :',X_Co)
    Y_Co,Starting_byte=Fixed_lengh_Char(Starting_byte,1)#;print('Position of Y direction of wafer :',Y_Co);
    return Starting_byte

def WIR(Starting_byte):    
    TestHeadnumber,Starting_byte=U1(Starting_byte,1)#;print("Test Head Number :",TestHeadnumber[0])
    SiteGourpNumber,Starting_byte=U1(Starting_byte,1)#;print('Site Group number :',SiteGourpNumber[0])
    DateEndTime,Starting_byte=U4(Starting_byte,1)#;print('Date and time first part tested :',DateEndTime[0])
    WfrId,Starting_byte=CN(Starting_byte,1)#;print('Local name of Pin :',WfrId[0]);
    return Starting_byte

def PIR(Starting_byte):
    TestHeadnumber,Starting_byte=U1(Starting_byte,1)#;print('Test Head number :',TestHeadnumber[0])
    TestSiteNumber,Starting_byte=U1(Starting_byte,1)#;print('Test Site Number :',TestSiteNumber[0])
    PartFullInfo[1].append(TestHeadnumber[0]);PartFullInfo[2].append(TestSiteNumber[0]);
    return Starting_byte

def PTR(Starting_byte):
    #print(Starting_byte,End_Record_Byte)
    TestNumber,Starting_byte=U4(Starting_byte,1)#;print('Test number :',TestNumber)
    TestHeadNumber,Starting_byte=U1(Starting_byte,1)#;print('Test Head Number :',TestHeadNumber)
    SiteNumber,Starting_byte=U1(Starting_byte,1)#;print('Site Number :',SiteNumber) 
    bytecode,Starting_byte=Fixed_Lenght_BitEncoded_data(Starting_byte,1)#;print('Ref of test flag :',bin(int.from_bytes(bytecode[0], byteorder=sys.byteorder)))
    TestFlag,Starting_byte=I1(Starting_byte-1,1)#;print('Test flag :',TestFlag)
    bytecode,Starting_byte=Fixed_Lenght_BitEncoded_data(Starting_byte,1)#;print('Ref of Peamatrice flag :',bin(int.from_bytes(bytecode[0], byteorder=sys.byteorder)))
    ParamFlag,Starting_byte=I1(Starting_byte-1,1)#;print('Parametric flag :',ParamFlag)
    TestResult,Starting_byte=R4(Starting_byte,1)#;print('Test result :',TestResult)
    TestName,Starting_byte=CN(Starting_byte,1)#;print('Test Discription:',TestName)
    AlaramName,Starting_byte=CN(Starting_byte,1)#;print('Alaram name :',AlaramName)
    if TestNumber[0] not in TestNumbers:
        bytecode,Starting_byte=Fixed_Lenght_BitEncoded_data(Starting_byte,1)#;print('Ref of test flag :',bin(int.from_bytes(bytecode[0], byteorder=sys.byteorder)))
        OptFlag,Starting_byte=I1(Starting_byte-1,1)#;print('Optional Data Flag :',OptFlag)
        TRSE,Starting_byte=I1(Starting_byte,1)#;print('Test Result Scaling exponent :',TRSE)
        LLSE,Starting_byte=I1(Starting_byte,1)#;print('Low limit scaling exponent :',LLSE)
        HLSE,Starting_byte=I1(Starting_byte,1)#;print('High limit scaling exponent :',HLSE)
        LowLim,Starting_byte=R4(Starting_byte,1)#;print('Low Limit :',LowLim)
        HighLim,Starting_byte=R4(Starting_byte,1)#;print('High limit :',HighLim)
        TestUnit,Starting_byte=CN(Starting_byte,1)#;print('Test Units :',TestUnit)
        CRFS,Starting_byte=CN(Starting_byte,1)#;print('C result Fmt string :',CRFS)
        CLLFS,Starting_byte=CN(Starting_byte,1)#;print('C Low lim Fmt string:',CLLFS)
        CHLFS,Starting_byte=CN(Starting_byte,1)#;print('C High Lim Fmt string :',CHLFS)
        LowSpec,Starting_byte=R4(Starting_byte,1)#;print('Low Spec Value :',LowSpec)
        HighSpec,Starting_byte=R4(Starting_byte,1)#;print('High Spec value :',HighSpec)    
    if (TestNumber[0] in TestNumbers and len(Test_Flag_Details)>1):
        LowLim=Test_Flag_Details[TestNumber[0]][4]
        HighLim=Test_Flag_Details[TestNumber[0]][5]
        TestUnit=Test_Flag_Details[TestNumber[0]][6]
        Test_Details[TestNumber+SiteNumber]=[TestNumber[0],TestName[0],LowLim,HighLim,TestResult[0],TestUnit]
        Test_Flag_Details[TestNumber+SiteNumber]=[Test_Flag_Details[TestNumber[0]][0],Test_Flag_Details[TestNumber[0]][1],Test_Flag_Details[TestNumber[0]][2],Test_Flag_Details[TestNumber[0]][3],Test_Flag_Details[TestNumber[0]][4],Test_Flag_Details[TestNumber[0]][5],Test_Flag_Details[TestNumber[0]][6],Test_Flag_Details[TestNumber[0]][7],Test_Flag_Details[TestNumber[0]][8],Test_Flag_Details[TestNumber[0]][9],Test_Flag_Details[TestNumber[0]][10],Test_Flag_Details[TestNumber[0]][11]]
        x=TestNumbers.index(int(TestNumber[0]));y=len(FullTestDetails[x]) ;z=len(PartFullInfo[1])
        if (z-y==1):            
            if (PartFullInfo[1][y]==TestHeadNumber[0] and PartFullInfo[2][y]==SiteNumber[0]):
                FullTestDetails[x].append(TestResult[0]);return Starting_byte#;pdb.set_trace()
        elif (z-y>1):                 
            for i in range(y,z):
                if (PartFullInfo[1][i]==TestHeadNumber[0] and PartFullInfo[2][i]== SiteNumber[0]):                    
                    FullTestDetails[x].append(TestResult[0]);return Starting_byte;break#;pdb.set_trace()
                elif (PartFullInfo[1][i]!=TestHeadNumber[0] or PartFullInfo[2][i]!=SiteNumber[0]):                    
                    FullTestDetails[x].append("")#;return Starting_byte#;pdb.set_trace()
    elif TestNumber[0] not in TestNumbers:
        if TestUnit=='':
            TestUnit=(b'',)        
        Test_Details[TestNumber[0]]=[TestNumber[0],TestName[0].decode("utf-8") ,LowLim[0],HighLim[0],TestUnit[0].decode("utf-8") ]
        Test_Flag_Details[TestNumber[0]]=[OptFlag[0],TRSE[0],LLSE,HLSE[0],LowLim[0],HighLim[0],TestUnit[0].decode("utf-8") ,CRFS[0].decode("utf-8") ,CLLFS[0].decode("utf-8") ,CHLFS[0].decode("utf-8") ,LowSpec[0],HighSpec[0]]
        TestNumbers.append(TestNumber[0])             
        FullTestDetails.append(TestNumber[0]);x=TestNumbers.index(int(TestNumber[0]))
        FullTestDetails[x]=[Test_Details[TestNumber[0]],TestResult[0]];
        return Starting_byte

def MPR(Starting_byte):
    TestNumber,Starting_byte=U4(Starting_byte,1);print('Test Number:',TestNumber)
    TestHeadNumber,Starting_byte=U1(Starting_byte,1);print('Head number:',TestHeadNumber)
    SiteNumber,Starting_byte=U1(Starting_byte,1);print('Site Number:',SiteNumber)
    TestFlag,Starting_byte=I1(Starting_byte,1);print('Test flag:',TestFlag)
    ParamFlag,Starting_byte=I1(Starting_byte,1);print('Parm flag:',ParamFlag)
    Rtn_Icnt,Starting_byte=U2(Starting_byte,1);print('count of J:',Rtn_Icnt)
    Rslt_cnt,Starting_byte=U2(Starting_byte,1);print('count of k',Rslt_cnt)
    Rtn_Stat,Starting_byte=N1(Starting_byte,Rtn_Icnt);print('arry retrn stat:',Rtn_Stat)
    TestResult,Starting_byte=R4(Starting_byte,Rslt_cnt[0]);print('Resturned result:',TestResult)
    TestName,Starting_byte=CN(Starting_byte,1);print('Test Lbl:',TestName)
    AlaramName,Starting_byte=CN(Starting_byte,1);print('Name of alaram:',AlaramName)
    #Corresponding data:
    OptFlag,Starting_byte=I1(Starting_byte,1);print('OPT_FLAG',OptFlag)
    TRSE,Starting_byte=I1(Starting_byte,1);print('RES_SCAL',TRSE)
    LLSE,Starting_byte=I1(Starting_byte,1);print('LLM_SCAL',LLSE)
    HLSE,Starting_byte=I1(Starting_byte,1);print('Hlm Scal',HLSE)
    LowLim,Starting_byte=R4(Starting_byte,1);print('Lo lim',LowLim)
    HighLim,Starting_byte=R4(Starting_byte,1);print('Hi lim',HighLim)
    Start_in,Starting_byte=R4(Starting_byte,1);print('Start_in:',Start_in)
    Incr_in,Starting_byte=R4(Starting_byte,1);print('Incr_in:',Incr_in)
    Rtn_indx,Starting_byte=U2(Starting_byte,Rtn_Icnt[0]);print('Rtn_indx',Rtn_indx)
    TestUnit,Starting_byte=CN(Starting_byte,1);print('Units',TestUnit)
    Units_in,Starting_byte=CN(Starting_byte,1);print('Unitsin',Units_in)
    CRFS,Starting_byte=CN(Starting_byte,1);print('C_Resfmt',CRFS)
    CLLFS,Starting_byte=CN(Starting_byte,1);print('C_llmfmt',CLLFS)
    CHLFS,Starting_byte=CN(Starting_byte,1);print('C_Hlmfmt',CHLFS)
    LowSpec,Starting_byte=R4(Starting_byte,1);print('Lo_spec',LowSpec)
    HighSpec,Starting_byte=R4(Starting_byte,1);print('Hi_spec',HighSpec)

    if (TestNumber[0] in TestNumbers and len(Test_Flag_Details)>1):
        LowLim=Test_Flag_Details[TestNumber[0]][4]
        HighLim=Test_Flag_Details[TestNumber[0]][5]
        TestUnit=Test_Flag_Details[TestNumber[0]][6]
        Test_Details[TestNumber+SiteNumber]=[TestNumber[0],TestName[0],LowLim,HighLim,TestResult[0],TestUnit,SiteNumber[0],TestFlag[0]]
        Test_Flag_Details[TestNumber+SiteNumber]=[Test_Flag_Details[TestNumber[0]][0],Test_Flag_Details[TestNumber[0]][1],Test_Flag_Details[TestNumber[0]][2],
                                                  Test_Flag_Details[TestNumber[0]][3],Test_Flag_Details[TestNumber[0]][4],Test_Flag_Details[TestNumber[0]][5],
                                                  Test_Flag_Details[TestNumber[0]][6],Test_Flag_Details[TestNumber[0]][7],Test_Flag_Details[TestNumber[0]][8],
                                                  Test_Flag_Details[TestNumber[0]][9],Test_Flag_Details[TestNumber[0]][10],Test_Flag_Details[TestNumber[0]][11]]
        x=TestNumbers.index(int(TestNumber[0]));y=len(FullTestDetails[x]) ;z=len(PartFullInfo[1])
        if (z-y==1):            
            if (PartFullInfo[1][y]==TestHeadNumber[0] and PartFullInfo[2][y]==SiteNumber[0]):
                FullTestDetails[x].append(TestResult[0]);return Starting_byte#;pdb.set_trace()
        elif (z-y>1):                 
            for i in range(y,z):
                if (PartFullInfo[1][i]==TestHeadNumber[0] and PartFullInfo[2][i]== SiteNumber[0]):                    
                    FullTestDetails[x].append(TestResult[0]);return Starting_byte;break#;pdb.set_trace()
                elif (PartFullInfo[1][i]!=TestHeadNumber[0] or PartFullInfo[2][i]!=SiteNumber[0]):                    
                    FullTestDetails[x].append("")#;return Starting_byte#;pdb.set_trace()
    elif TestNumber[0] not in TestNumbers:
        if TestUnit=='':
            TestUnit=(b'',)        
        Test_Details[TestNumber[0]]=[TestNumber[0],TestName[0].decode("utf-8") ,LowLim[0],HighLim[0],TestUnit[0].decode("utf-8") ]
                                     
        Test_Flag_Details[TestNumber[0]]=[OptFlag[0],TRSE[0],LLSE,HLSE[0],LowLim[0],HighLim[0],TestUnit[0].decode("utf-8")
                                          ,CRFS[0].decode("utf-8"),CLLFS[0].decode("utf-8"),CHLFS[0].decode("utf-8") ,LowSpec[0],HighSpec[0]]
        TestNumbers.append(TestNumber[0])             
        FullTestDetails.append(TestNumber[0]);x=TestNumbers.index(int(TestNumber[0]))
        FullTestDetails[x]=[Test_Details[TestNumber[0]],TestResult[0]];        
    return Starting_byte

def FTR(Starting_byte):    
    TestNumber,Starting_byte=U4(Starting_byte,1)#;print('TestNumber :',TestNumber[0])
    #if TestNumber[0]==6000:
    #   print(Starting_byte-4);sys.exit(0)
    TestHeadNumber,Starting_byte=U1(Starting_byte,1)#;print('Test Head Number :',TestHeadNumber[0])
    SiteNumber,Starting_byte=U1(Starting_byte,1)#;print('Site Number :',SiteNumber[0])
    bytecode,Starting_byte=Fixed_Lenght_BitEncoded_data(Starting_byte,1)#;print('Ref of test flag :',bin(int.from_bytes(bytecode[0], byteorder=sys.byteorder)))
    TestFlag,Starting_byte=I1(Starting_byte-1,1)#;print('Test Flag :',TestFlag[0])
    if TestFlag[0]==0:
        TestResult=(1,)
    else :
        TestResult=(0,)
    OptFlag,Starting_byte=I1(Starting_byte,1)#;print('Optional Flag :',OptFlag[0])
    Cycl_Cnt,Starting_byte=U4(Starting_byte,1)#;print('Vector Cycle count :',Cycl_Cnt[0])
    Rel_V_Addr,Starting_byte=U4(Starting_byte,1)#;print('Relative vector address :',Rel_V_Addr[0])
    Rept_C_Vctr,Starting_byte=U4(Starting_byte,1)#;print('Vector Repeat count :',Rept_C_Vctr[0])
    Num_P_Fail,Starting_byte=U4(Starting_byte,1)#;print('Pin count with 1 or more Failures',Num_P_Fail[0])
    X_Fail_Adrs,Starting_byte=I4(Starting_byte,1)#;print('X Logical dev Fail address :',X_Fail_Adrs[0])
    Y_Fail_Adrs,Starting_byte=I4(Starting_byte,1)#;print('Y Logical dev Fail address :',Y_Fail_Adrs[0])
    Vect_offset,Starting_byte=I2(Starting_byte,1)#;print('Offset from vector of intrest :',Vect_offset[0])
    Rtn_PmrIndex_cnt,Starting_byte=U2(Starting_byte,1)#;print('PMR indexes return data count :',Rtn_PmrIndex_cnt[0])
    Pgm_StateIndex,Starting_byte=U2(Starting_byte,1)#;print('Programed state index count :',Pgm_StateIndex[0])
    if Rtn_PmrIndex_cnt[0]>0:    
        RTN_Index_ary,Starting_byte=U2(Starting_byte,Rtn_PmrIndex_cnt[0])#;print('Return PMR Array',RTN_Index_ary)
        RTN_State_ary,Starting_byte=U2(Starting_byte,Rtn_PmrIndex_cnt[0])#;print('Return State Array',RTN_State_ary,'check the record to solve it') # check the pdf need extract nibble data
    if Pgm_StateIndex[0]>0:
        Pgm_State_indx_ary,Starting_byte=U2(Starting_byte,Pgm_StateIndex[0])#;print('Program PMR Array',Pgm_State_indx_ary)
        Pgm_State_ary,Starting_byte=U2(Starting_byte,Rtn_PmrIndex_cnt[0])#;print('Program State Array',Pgm_State_ary,'check the record to solve it')
    Failpin,Starting_byte=DN(Starting_byte,1)#;print('Fail pin bit field :',Failpin,Starting_byte)
    VectNum,Starting_byte=CN(Starting_byte,1)#;print('Vect Module pattern name :',VectNum)
    Timesetname,Starting_byte=CN(Starting_byte,1)#;print('Time set name :',Timesetname)#[0].decode('utf-8'))
    opcode,Starting_byte=CN(Starting_byte,1)#;print('Vector Op code :',opcode)
    Test_Txt,Starting_byte=CN(Starting_byte,1)#;print('Des Text or lable:',Test_Txt)
    AlrmId,Starting_byte=CN(Starting_byte,1)#;print('Nmae of alaram :',AlrmId)
    ProgmTxt,Starting_byte=CN(Starting_byte,1)#;print('Addtional program info :',ProgmTxt)        
    RsltTxt,Starting_byte=CN(Starting_byte,1)#;print('Addtional result info :',RsltTxt)
    #if TestNumber[0] not in TestNumbers:
    Patrn_num,Starting_byte=U1(Starting_byte,1)#;print('Pattern generator number :',Patrn_num[0])
    SpinMap,Starting_byte=DN(Starting_byte,1)#;print('Bit map of enableed comprators :',SpinMap)
    if(TestNumber[0] in TestNumbers and len(Test_Flag_Details)>1 ):
        LowLim=(b'',)
        HighLim=(b'',)
        TestUnit=(b'',)
        #TestResult=(b'',)
        Test_Details[TestNumber[0]]=[TestNumber[0],Test_Txt[0].decode('utf-8') ,LowLim[0],HighLim[0],TestUnit[0].decode("utf-8") ]
        Test_Flag_Details[TestNumber[0]]=[OptFlag[0],Cycl_Cnt[0],Rel_V_Addr[0],Rept_C_Vctr[0],Num_P_Fail[0],X_Fail_Adrs[0],Y_Fail_Adrs[0],Vect_offset[0],Rtn_PmrIndex_cnt[0],Test_Txt[0].decode('utf-8')]
        x=TestNumbers.index(int(TestNumber[0]));y=len(FullTestDetails[x]) ;z=len(PartFullInfo[1])
        if (z-y==1):            
            if (PartFullInfo[1][y]==TestHeadNumber[0] and PartFullInfo[2][y]==SiteNumber[0]):
                FullTestDetails[x].append(TestResult[0]);return Starting_byte;
        elif (z-y>1):                 
            for i in range(y,z):
                if (PartFullInfo[1][i]==TestHeadNumber[0] and PartFullInfo[2][i]== SiteNumber[0]):                    
                    FullTestDetails[x].append(TestResult[0]);return Starting_byte;break
                elif (PartFullInfo[1][i]!=TestHeadNumber[0] or PartFullInfo[2][i]!=SiteNumber[0]):                    
                    FullTestDetails[x].append(" ")#;return Starting_byte;
    elif TestNumber[0] not in TestNumbers:        
        LowLim=(b'',)
        HighLim=(b'',)
        TestUnit=(b'',)
        #TestResult=(b'',)
        Test_Details[TestNumber[0]]=[TestNumber[0],Test_Txt[0].decode('utf-8') ,LowLim[0],HighLim[0],TestUnit[0].decode("utf-8")]
        Test_Flag_Details[TestNumber[0]]=[OptFlag[0],Cycl_Cnt[0],Rel_V_Addr[0],Rept_C_Vctr[0],Num_P_Fail[0],X_Fail_Adrs[0],Y_Fail_Adrs[0],Vect_offset[0],Rtn_PmrIndex_cnt[0],Test_Txt[0].decode('utf-8'),Patrn_num[0],SpinMap]
        TestNumbers.append(TestNumber[0])             
        FullTestDetails.append(TestNumber[0]);x=TestNumbers.index(int(TestNumber[0]))
        FullTestDetails[x]=[Test_Details[TestNumber[0]],TestResult[0]]
        return Starting_byte
def PRR(Starting_byte):    
    HeadNum,Starting_byte=U1(Starting_byte,1)#;print('Test Head Number :',HeadNum[0])
    SiteNum,Starting_byte=U1(Starting_byte,1)#;print('Test Site Number :',SiteNum[0])
    Part_Flag,Starting_byte=Fixed_Lenght_BitEncoded_data(Starting_byte,1)#;print('Part info Flag :',bin(int.from_bytes(Part_Flag[0], byteorder=sys.byteorder)))
    Part_Flag=bin(int.from_bytes(Part_Flag[0], byteorder=sys.byteorder))
    #if Part_Flag[0]== b'\n':        
    #    print(HeadNum[0],SiteNum[0],Starting_byte)
    #Part_Flag_1,Starting_byte=I1(Starting_byte-1,1)#;print('Part info Flag :',Part_Flag_1[0])
    Num_Test,Starting_byte=U2(Starting_byte,1)#;print('Number of tests executed :',Num_Test[0])
    HardBin,Starting_byte=U2(Starting_byte,1)#;print('Hardware Bin Number :',HardBin[0])
    SoftBin,Starting_byte=U2(Starting_byte,1)#;print('Software Bin Number :',SoftBin[0])
    XCo_ord,Starting_byte=I2(Starting_byte,1)#;print('X co-ordinate :',XCo_ord[0])
    YCo_ord,Starting_byte=I2(Starting_byte,1)#;print("Y Co-Oridinate :",YCo_ord[0])
    Testtime,Starting_byte=U4(Starting_byte,1)#;print('Test time in mil sec :',Testtime[0])
    PartId,Starting_byte=CN(Starting_byte,1)#;print('Part identification :',PartId[0].decode('utf-8'))
    #if Part_Flag[0]== b'\n':
    #    print(HeadNum[0],SiteNum[0],Part_Flag[0]);sys.exit(0)
    Part_Dis_Txt,Starting_byte=CN(Starting_byte,1)#;print('Part Description :',Part_Dis_Txt)
    PartFix,Starting_byte=BN(Starting_byte,1)#;print('Part repair Info :',PartFix)
    PartFullInfo[0].append(PartId[0].decode('utf-8'));PartFullInfo[3].append(Part_Flag);PartFullInfo[4].append(Num_Test[0])
    PartFullInfo[5].append(HardBin[0]);PartFullInfo[6].append(SoftBin[0]);PartFullInfo[7].append(XCo_ord[0]);PartFullInfo[8].append(YCo_ord[0])
    return Starting_byte
def WRR(Starting_byte):
    HeadNum,Starting_byte=U1(Starting_byte,1)#;print('Test Head Number:',HeadNum[0])
    Site_Grp,Starting_byte=U1(Starting_byte,1)#;print('Site Group Number:',Site_Grp[0])
    Finish_t,Starting_byte=U4(Starting_byte,1)#;print('Date and Time last part tested:',Finish_t[0])
    Part_Cnt,Starting_byte=U4(Starting_byte,1)#;print('Number of parts tested:',Part_Cnt[0])
    Rtst_Cnt,Starting_byte=U4(Starting_byte,1)#;print('Number of retested Parts :',Rtst_Cnt[0])
    Abrt_cnt,Starting_byte=U4(Starting_byte,1)#;print('Number of aborts during testing:',Abrt_cnt[0])
    Good_cnt,Starting_byte=U4(Starting_byte,1)#;print('Number of good parts:',Good_cnt[0])
    Func_Cnt,Starting_byte=U4(Starting_byte,1)#;print('Number of Functional tests:',Func_Cnt[0])
    Wafer_id,Starting_byte=CN(Starting_byte,1)#;print('Wafer id:',Wafer_id[0])
    Fabwf_id,Starting_byte=CN(Starting_byte,1)#;print('Fab WaferId:',Fabwf_id)
    Frame_id,Starting_byte=CN(Starting_byte,1)#;print('Wafer Frame Id:',Frame_id)
    Mask_id,Starting_byte=CN(Starting_byte,1)#;print('Wafer Mask id:',Mask_id)
    Usr_desc,Starting_byte=CN(Starting_byte,1)#;print('wafer description suplied by user:',Usr_desc)
    Exc_Desc,Starting_byte=CN(Starting_byte,1)#;print('Wafer description suplied by exec:',Exc_Desc)
    return Starting_byte
def TSR(Starting_byte):
    HeadNum,Starting_byte=U1(Starting_byte,1)#;print('Test Head Num:',HeadNum[0])
    SiteNum,Starting_byte=U1(Starting_byte,1)#;print('Test Site Numebr:',SiteNum[0])
    Test_type,Starting_byte=Fixed_lengh_Char(Starting_byte,1)#;print('Test type:',Test_type)
    Test_Num,Starting_byte=U4(Starting_byte,1)#;print('Test Number:',Test_Num)
    Exec_Cnt,Starting_byte=U4(Starting_byte,1)#;print('Nunber of test Executions:',Exec_Cnt)
    Fail_Cnt,Starting_byte=U4(Starting_byte,1)#;print('Number of test failures:',Fail_Cnt)
    Alarm_Cnt,Starting_byte=U4(Starting_byte,1)#;print('Number of alarmed tests:',Alarm_Cnt)
    Test_nam,Starting_byte=CN(Starting_byte,1)#;print('Test Name:',Test_nam[0])
    Seq_nam,Starting_byte=CN(Starting_byte,1)#;print('Frogram flow name:',Seq_nam)
    Test_lbl,Starting_byte=CN(Starting_byte,1)#;print('Test lable:',Test_lbl)
    Opt_Flag,Starting_byte=I1(Starting_byte,1)#;print('Optional data flag:',Opt_Flag)
    Test_tim,Starting_byte=R4(Starting_byte,1)#;print('avg test execu time:',Test_tim)
    Test_min,Starting_byte=R4(Starting_byte,1)#;print('Lowest test result value:',Test_min)
    Test_max,Starting_byte=R4(Starting_byte,1)#;print('highst test result value:',Test_max)
    Test_sums,Starting_byte=R4(Starting_byte,1)#;print('Sum of test result values:',Test_sums)
    Test_sqrs,Starting_byte=R4(Starting_byte,1)#;print('Sum of squares of test result val:',Test_sqrs)
    #Inserting the data into list
    TestSummary_Report[0].append(HeadNum[0]);TestSummary_Report[1].append(SiteNum[0]);TestSummary_Report[2].append(Test_type[0])
    TestSummary_Report[3].append(Test_Num[0]);TestSummary_Report[4].append(Exec_Cnt[0]);TestSummary_Report[5].append(Fail_Cnt[0])
    TestSummary_Report[6].append(Alarm_Cnt[0]);TestSummary_Report[7].append(Test_nam[0]);TestSummary_Report[8].append(Seq_nam)
    TestSummary_Report[9].append(Test_lbl);TestSummary_Report[10].append(Opt_Flag[0]);TestSummary_Report[11].append(Test_tim[0])
    TestSummary_Report[12].append(Test_min[0]);TestSummary_Report[13].append(Test_max[0]);TestSummary_Report[14].append(Test_sums[0])
    TestSummary_Report[15].append(Test_sqrs[0])
    return Starting_byte

def HBR(Starting_byte):
    HeadNum,Starting_byte=U1(Starting_byte,1)#;print('Test Head Num:',HeadNum[0])
    SiteNum,Starting_byte=U1(Starting_byte,1)#;print('Test Site Numebr:',SiteNum[0])
    HbinNum,Starting_byte=U2(Starting_byte,1)#;print('Hardware bin:',HbinNum)
    Hbin_Cnt,Starting_byte=U4(Starting_byte,1)#;print('Number of parts in bin:',Hbin_Cnt)
    Hbin_Pf,Starting_byte=Fixed_lengh_Char(Starting_byte,1)#;print('Pass/Fail Indication:',Hbin_Pf)
    Hbin_nam,Starting_byte=CN(Starting_byte,1)#;print('Name of hardware bin:',Hbin_nam)
    #Writing into list
    Hbin_sumary[0].append(HeadNum[0]);Hbin_sumary[1].append(SiteNum[0]);Hbin_sumary[2].append(HbinNum[0])
    Hbin_sumary[3].append(Hbin_Cnt[0]);Hbin_sumary[4].append(Hbin_Pf[0]);Hbin_sumary[5].append(Hbin_nam[0])
    return Starting_byte

def SBR(Starting_byte):
    HeadNum,Starting_byte=U1(Starting_byte,1)#;print('Test Head Num:',HeadNum[0])
    SiteNum,Starting_byte=U1(Starting_byte,1)#;print('Test Site Numebr:',SiteNum[0])
    SbinNum,Starting_byte=U2(Starting_byte,1)#;print('Hardware bin:',SbinNum)
    Sbin_Cnt,Starting_byte=U4(Starting_byte,1)#;print('Number of parts in bin:',Sbin_Cnt)
    Sbin_Pf,Starting_byte=Fixed_lengh_Char(Starting_byte,1)##;print('Pass/Fail Indication:',Sbin_Pf)
    Sbin_nam,Starting_byte=CN(Starting_byte,1)#;print('Name of hardware bin:',Sbin_nam)
    #Writing into list
    Sbin_sumary[0].append(HeadNum[0]);Sbin_sumary[1].append(SiteNum[0]);Sbin_sumary[2].append(SbinNum[0])
    Sbin_sumary[3].append(Sbin_Cnt[0]);Sbin_sumary[4].append(Sbin_Pf[0]);Sbin_sumary[5].append(Sbin_nam[0])
    return Starting_byte
def PCR(Starting_byte):
    HeadNum,Starting_byte=U1(Starting_byte,1)#;print('Test Head Num:',HeadNum[0])
    SiteNum,Starting_byte=U1(Starting_byte,1)#;print('Test Site Numebr:',SiteNum[0])
    Part_cnt,Starting_byte=U4(Starting_byte,1)#;print('Num of parts:',Part_cnt[0])
    Rtst_Cnt,Starting_byte=U4(Starting_byte,1)#;print('Num of restested parts:',Rtst_Cnt)
    Abrt_Cnt,Starting_byte=U4(Starting_byte,1)#;print('Number of aborts during testing:',Abrt_Cnt)
    Good_Cnt,Starting_byte=U4(Starting_byte,1)#;print('Number of good parts:',Good_Cnt)
    Func_Cnt,Starting_byte=U4(Starting_byte,1)#;print('Number of Func parts tested',Func_Cnt)
    #Wrting the data into list\
    PCR_Rec_Summary[0].append(HeadNum[0]);PCR_Rec_Summary[1].append(SiteNum[0]);PCR_Rec_Summary[2].append(Part_cnt[0])
    PCR_Rec_Summary[3].append(Rtst_Cnt[0]);PCR_Rec_Summary[4].append(Abrt_Cnt[0]);PCR_Rec_Summary[5].append(Good_Cnt[0])
    PCR_Rec_Summary[6].append(Func_Cnt[0])
    return Starting_byte

def MRR(Starting_byte):
    Finist_Time,Starting_byte=U4(Starting_byte,1)#;print('finsish time:',Finist_Time[0])
    Disp_Cod,Starting_byte=Fixed_lengh_Char(Starting_byte,1)#;print('Lot Disposition code:',Disp_Cod)
    USr_Desc,Starting_byte=CN(Starting_byte,1)#;print('Lot dscription suplied by user:',USr_Desc)
    Exc_Desc,Starting_byte=CN(Starting_byte,1)#;print('Lot description suplied by sys',Exc_Desc)
    return Starting_byte
def BPS(Starting_byte):
    Seq_name,Starting_byte=CN(Starting_byte,1)#;print('Program sec rec',Seq_name)
    return(Starting_byte)

def DTR(Starting_byte):
    TEXT_DAT,Starting_byte=CN(Starting_byte,1)#;print('Ascii text sring',TEXT_DAT)
    return(Starting_byte)

def EPS(Starting_byte):
    print(Starting_byte+'this is EPS record check if you want')
    return(Starting_byte)

def GDR(Starting_byte):
    Fld_Cnt,Starting_byte=U2(Starting_byte,1)#;print('countof data fileds in record',Fld_Cnt)
    for i in range(Fld_Cnt[0]):
        Gen_Data,Starting_byte=I1(Starting_byte,1)#;print('Gen data %i'%i ,Gen_Data)
        Rc=VN_MAP[str(Gen_Data[0])]
        temp,Starting_byte=Rc(Starting_byte,1)#;print(temp) 
        final=('Gen data %i'%i ,temp[0])#;print(final)
        GDR_Summary.append(final)
    return(Starting_byte)

def PGR(Starting_byte):
    Grp_index,Starting_byte=U2(Starting_byte,1)#;print('Uniq index associated with pin grp',Grp_index)
    GRP_NAM,Starting_byte=CN(Starting_byte,1)#;print('name of pin grop',GRP_NAM)
    INDX_CNT,Starting_byte=U2(Starting_byte,1)#;print('cont of k ',INDX_CNT)
    PMR_INDX,Starting_byte=U2(Starting_byte,INDX_CNT[0])#;print('arry of indx for pins in grp',PMR_INDX)
    return(Starting_byte)

def PLR(Starting_byte):
    Grp_Cnt,Starting_byte=U2(Starting_byte,1)#;print('count of k',Grp_Cnt)
    Grp_indx,Starting_byte=U2(Starting_byte,Grp_Cnt[0])#;print('Grp_indx',Grp_indx)
    GRP_MODE,Starting_byte=U2(Starting_byte,Grp_Cnt[0])#;print('GRP_MODE',GRP_MODE)
    GRP_RADX,Starting_byte=U1(Starting_byte,Grp_Cnt[0])#;print('GRP_RADX',GRP_RADX)
    PGM_CHAR,Starting_byte=CN(Starting_byte,Grp_Cnt[0])#;print('PGM_CHAR',PGM_CHAR)
    RTN_CHAR,Starting_byte=CN(Starting_byte,Grp_Cnt[0])#;print('RTN_CHAR',RTN_CHAR)
    PGM_CHAL,Starting_byte=CN(Starting_byte,Grp_Cnt[0])#;print('PGM_CHAL',PGM_CHAL)
    RTN_CHAL,Starting_byte=CN(Starting_byte,Grp_Cnt[0])#;print('RTN_CHAL',RTN_CHAL)
    return(Starting_byte)

def RDR(Starting_byte):
    Num_bins,Starting_byte=U2(Starting_byte,1)#;print('nuber of bins k ',Num_bins)
    RTST_BIN,Starting_byte=U2(Starting_byte,Num_bins[0])#;print('Grp_indx',RTST_BIN)
    return Starting_byte
def VUR(Starting_byte):
    print(Starting_byte,Record_name,'refer to document on this')
    #break
def PSR(Starting_byte):
    print(Starting_byte,Record_name,'refer to document on this')
    #break
def NMR(Starting_byte):
    print(Starting_byte,Record_name,'refer to document on this')
    #break
def CNR(Starting_byte):
    print(Starting_byte,Record_name,'refer to document on this')
    #break
def SSR(Starting_byte):
    print(Starting_byte,Record_name,'refer to document on this')
    #break
def SCR(Starting_byte):
    print(Starting_byte,Record_name,'refer to document on this')
    #break
def STR(Starting_byte):
    print(Starting_byte,Record_name,'refer to document on this')
    #break
    
#reading the data
#@staticmethod
def Encodethedata(Starting_byte):  
    Starting_byte=Starting_byte    
    while Starting_byte<len(STDF_Data):        
        Starting_byte=Record_header(Starting_byte) 
        prgrs=math.ceil((Starting_byte/len(STDF_Data))*100)
        try:                
            #if prgrs>=1:progress['value']=prgrs;print("%s of 100 is complted"%prgrs)
            if Record_name==['FAR']:
                Starting_byte=FAR(Starting_byte)
            elif Record_name==['ATR']:
                Starting_byte=ATR(Starting_byte)
            elif Record_name==['MIR']:
                Starting_byte=MIR(Starting_byte)
                Starting_byte=End_Record_Byte
            elif Record_name==['SDR']:
                Starting_byte=SDR(Starting_byte)
            elif Record_name==['PMR']:
                Starting_byte=PMR(Starting_byte)
            elif Record_name==['WCR']:
                Starting_byte=WCR(Starting_byte)
            elif Record_name==['WIR']:
                Starting_byte=WIR(Starting_byte)
            elif Record_name==['PIR']:
                Starting_byte=PIR(Starting_byte)
            elif Record_name==['PTR']:
                Starting_byte=PTR(Starting_byte)
            elif Record_name==['FTR']:
                Starting_byte=FTR(Starting_byte)
            elif Record_name==['PRR']:
                Starting_byte=PRR(Starting_byte)
            elif Record_name==['WRR']:
                Starting_byte=WRR(Starting_byte)
            elif Record_name==['TSR']:
                Starting_byte=TSR(Starting_byte)
            elif Record_name==['HBR']:
                Starting_byte=HBR(Starting_byte)
            elif Record_name==['SBR']:
                Starting_byte=SBR(Starting_byte)
            elif Record_name==['PCR']:
                Starting_byte=PCR(Starting_byte)  
            elif Record_name==['MRR']:
                Starting_byte=MRR(Starting_byte)
            elif Record_name==['BPS']:
                Starting_byte=BPS(Starting_byte)
            elif Record_name==['DTR']:
                Starting_byte=DTR(Starting_byte)
            elif Record_name==['EPS']:
                Starting_byte=EPS(Starting_byte)
            elif Record_name==['GDR']:
                Starting_byte=GDR(Starting_byte)
            elif Record_name==['PGR']:
                Starting_byte=PGR(Starting_byte)
            elif Record_name==['PLR']:
                Starting_byte=PLR(Starting_byte)
            elif Record_name==['RDR']:
                Starting_byte=RDR(Starting_byte)
            elif Record_name==['MPR']:
                Starting_byte=MPR(Starting_byte)
            elif Record_name==['VUR']:
                #Starting_byte=VUR(Starting_byte)
                Starting_byte=End_Record_Byte;print('VUR RECORD USED')                
            elif Record_name==['NMR']:
                #Starting_byte=NMR(Starting_byte)
                Starting_byte=End_Record_Byte;print('NMR RECORD USED')
            elif Record_name==['PSR']:
                #Starting_byte=PSR(Starting_byte)
                Starting_byte=End_Record_Byte;print('PSR RECORD USED')
            elif Record_name==['CNR']:
                #Starting_byte=CNR(Starting_byte)
                Starting_byte=End_Record_Byte;print('CNR RECORD USED')
            elif Record_name==['SSR']:
                #Starting_byte=SSR(Starting_byte)
                Starting_byte=End_Record_Byte;print('SSR RECORD USED')
            elif Record_name==['SCR']:
                #Starting_byte=SCR(Starting_byte)
                Starting_byte=End_Record_Byte;print('SCR RECORD USED')
            elif Record_name==['STR']:
                #Starting_byte=STR(Starting_byte)  
                Starting_byte=End_Record_Byte;print('STR RECORD USED')                  
            else:
                print(Record_name,Starting_byte)#;break
        except:
            print(Record_name,Starting_byte)
    Starting_byte>=len(STDF_Data)
    print('File reading complted');return
def Convert_to_CSV(input):
    output=input
    output=output[0:len(output)-5]+'.csv'
    with open(output,'w') as F:
        for i in range(0 , len(PartFullInfo)):
             print(PartFullInfo[i],file=F)
        for i in range(1 , len(FullTestDetails)):
             print(FullTestDetails[i],file=F)
        progress['value']=100
        
        #print('CSV file created with file name %s'%output)
        
    
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter, tkinter.filedialog, tkinter.constants 
from tkinter.filedialog import askopenfilename
#from Stdf_Reader import *

def _Browse_File():
    filename = tkinter.filedialog.askopenfilename(parent=Stdf_Parser_Form,title='Choose a file')
    yourName.insert(0,filename)
    clicked=True   
    
def Start_process():
    Input_file=yourName.get()
    if Input_file!="":
        ReadFile(Input_file)
        Encodethedata(0)
        Convert_to_CSV(Input_file)
        messagebox.showinfo("Successful", "STDF to CSV Convertion is completed")
        Stdf_Parser_Form.destroy()
    else:
        messagebox.showinfo("Error", "Please Browse a File")

Stdf_Parser_Form=Tk()
Stdf_Parser_Form.geometry("510x90")
Stdf_Parser_Form.wm_iconbitmap('C:/Users/2360/Desktop/Tes_logo.ico')
Stdf_Parser_Form.title("Stdf_to_CSV")
l=LabelFrame(Stdf_Parser_Form,text="Browse the file",width=500,height=80)
l.pack( expand="yes")
l.place(x=7,y=3)
#Browse Button
custName = StringVar(None)
yourName = Entry(l, textvariable=custName)
yourName.pack(padx = 20, pady = 20,anchor='n')
yourName.place(y = 0, x = 70, width = 350, height = 20)
browsebutton = Button(l, text="Browse", command=_Browse_File,width=7)
browsebutton.pack(side=RIGHT)   
browsebutton.place(y = -2, x = 430)

global Input_file
Input_file=yourName.get()#input("Enter the file name & path")#main_Lot_1_Oct_12_17h06m09s
#Okay button
ok=Button(l,text="OK",command=Start_process,width=5)
ok.pack()
ok.place(x=370,y=30)
#Quit Button
quit=Button(l,text="Quit",width=5,command=Stdf_Parser_Form.destroy)
quit.pack()
quit.place(x=420,y=30)
#Lable
label2=Label(l, text="Select File:")
label2.pack()
label2.place(y = -2, x = 5)
#Progress Bar
progress = ttk.Progressbar(l, orient="horizontal",length=350, mode="determinate")
progress.pack()
progress.place(x=8,y=30)
Stdf_Parser_Form.mainloop()