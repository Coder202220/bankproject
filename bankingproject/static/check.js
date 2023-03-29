$(document).ready(function()
    {
      $('.chkbox').click(function()
      {
        var text="";
        $('.chkbox:checked').each(function()
          {
            text += $(this).val() + ',';
            });
        text= text.substring(0,text.length-1);
        $('#chktext').val(text);
          });
           $('#but1').click(function()
            {
              confirm("Applicaton accepted\nclick ok to return home page");
            });
     });