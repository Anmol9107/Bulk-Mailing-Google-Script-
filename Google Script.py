function myFunction() {
  
  
  var sheetname = "Startup-FollowUps"     
  var ss = SpreadsheetApp.getActiveSpreadsheet(); 
  var sheet = ss.getSheetByName(sheetname);
    
  if (sheet.getRange(sheet.getMaxRows(),1).getValue() != "") {
     var lastrow = sheet.getMaxRows()    
  } else {
     var count = 0
     for (var i = 0; i < sheet.getMaxRows(); i++) {
        if (sheet.getRange(sheet.getMaxRows()-i,1).getValue() != "") {
        var lastrow = sheet.getMaxRows()-i
        break;
        }  
     }
  }
 
 for (var row = 2; row <=lastrow ; row++) 
  { 
  var firstname = sheet.getRange(row,2,1,1).getValue();
  var lastname = sheet.getRange(row,3,1,1).getValue();
  var number = sheet.getRange(row,4,1,1).getValue();
  var email = sheet.getRange(row,5,1,1).getValue();
  var company = sheet.getRange(row,6,1,1).getValue();
  var stage = sheet.getRange(row,7,1,1).getValue();
  var task = sheet.getRange(row,8,1,1).getValue();
  var comments = sheet.getRange(row,9,1,1).getValue();
  var additionalline= sheet.getRange(row, 10, 1, 1).getValue();
   
    if (task== "IntroSend" && stage=="")
    {
    var message =   * Insert here the message you want to send *
	

    
     // MailApp.sendEmail (email, "  * Insert the E-Mail Subject here *  ", "", {cc: "  *  CC Email  *  ",htmlBody: message,});  
      MailApp.sendEmail ({
        to: email, 
        subject: "  * Insert the E-Mail Subject here *  ", 
        cc:"  *  CC Email*  ",
        htmlBody: message, 
        
      }
      );  
    
      sheet.getRange(row,7,1,1).setValue("Email Sent");
    } 
  }
}