from selenium.webdriver.common.by import By

class Locator:
    
#login Page Locators
    userNameElement = (By.ID,"email")
    passwordElemenmt =(By.ID,"password")
    submittButtonElement=(By.XPATH,"//button[@type='submit']")
    
    InvalidEmailerrMsg =(By.CLASS_NAME,"errorMsg")
    ErrorMessage = (By.XPATH,"//div[@id='toaster']/div[@class='alert alert-danger alert-dismissible fade show']")
    
#Home page element after valid login
    imageButton = (By.XPATH,"//img[@class='userImage']")
    LogOutButton =(By.XPATH,"//a[contains(text(),'Logout')]")
    

#Sign Up Page Element 
    createAccountLink =(By.XPATH,"//a[contains(text(),'Create account')]")
    firstName = (By.XPATH,"//input[@id='fname']")
    lastName = (By.XPATH,"//input[@id='lname']")
    emailAddress = (By.XPATH,"//input[@id='email']")
    password=(By.XPATH,"//input[@id='password']")
    confirmPassword=(By.XPATH,"//input[@id='confirmPassword']")
    CreateButton=(By.XPATH,"//button[@type='submit']")
    
#After perform sign Up LogIn should be appear 
    
    logInLink = (By.XPATH,"//a[contains(text(),'Login')]")

#SettingPage GoogleDrive Elemenet
    SettingImageButton=(By.XPATH,"//img[@class='userImage']")
    settingOption =(By.XPATH,"//a[contains(text(),'Settings')]")
    googleDriveButton =(By.XPATH,"//a[contains(text(),'Google drive ')]")
    googledriveEmail = (By.XPATH,"//input[@type='email']")
    googledrivePass =(By.XPATH,"//input[@type='password']")
    GdriveUserNextButton =(By.XPATH,"(//span[@class='RveJvd snByac'])[1]")
    GdrivePassNextButton=(By.XPATH,"(//span[@class='RveJvd snByac'])[1]")
    advanceLink = (By.XPATH,"//a[contains(text(),'Advance')]")
 #  goToI2chainInfoUnsafe ="//a[contains(text(),'Go to i2chain.info(unsafe)')]"
 #  goToI2chainInfoUnsafe ="//a[starts-with(text(),'Go')]"
    goToI2chainInfoUnsafe=(By.XPATH,"(//a[@class='xTI6Gf vh6Iad'])[2]")
    AllowButton = (By.XPATH,"(//span[@class='RveJvd snByac'])[1]")
    GDriveConSucMes =(By.XPATH,"//div[@class='alert alert-danger alert-dismissible fade show']")
    GDriveLogOutButton=(By.XPATH,"//button[@class='auth-logput-btn']")
    GDriveLogoutYesButton=(By.XPATH,"//button[@class='btn btn-primary']")

#Setting page OneDrive element
    SettingImageButton = (By.XPATH, "//img[@class='userImage']")
    settingOption = (By.XPATH, "//a[contains(text(),'Settings')]")
    OneDriveButton =(By.XPATH,"//a[contains(text(),'One drive ')]")
    OneDriveEmail = (By.XPATH,"//input[@type='email']")
    OneDriveUserNextButton =(By.XPATH,"//input[@type='submit']")
    OneDrivePass =(By.XPATH,"//input[@type='password']")

#Setting page DropbBox Element for connect dropbox drive

    SettingImageButton = (By.XPATH, "//img[@class='userImage']")
    settingOption = (By.XPATH, "//a[contains(text(),'Settings')]")
    DropBoxButton =(By.XPATH,"//a[contains(text(),'Dropbox ')]")
    signWithGoogle =(By.XPATH,"(//div[@class='sign-in-text'])[1]")
    dropBoxEmail = (By.XPATH,"//input[@type='email']")
    NextButtonEmail=(By.XPATH,"(//span[@class='RveJvd snByac'])[1]")
    dropBoxPassword=(By.XPATH,"//input[@type='password']")
    dropBoxNextButtonPass=(By.XPATH,"(//span[@class='RveJvd snByac'])[1]")
    dropBoxLogOutButton=(By.XPATH,"//button[@class='auth-logput-btn']")

