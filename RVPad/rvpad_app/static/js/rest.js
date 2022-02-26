$(document).ready(function(){
    $('#name').keyup(function(){
        var data = $("#restForm").serialize()   // capture all the data in the form in the variable data
        $.ajax({
            method: "POST",   // we are using a post request here, but this could also be done with a get
            url: "/rvpad/name",
            data: data
        })
        .done(function(res){
             $('#nameMsg').html(res)  // manipulate the dom when the response comes back
             $('#nameMsg,.success').css('color','#54f542')
             $('#nmaeMsg,.error').css('color','#f5ed05')
        })
    })
})