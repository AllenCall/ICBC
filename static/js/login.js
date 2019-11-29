$(function () {
    $('#submit').click(function (event) {
        event.preventDefault()
        var email = $('input[name = email]').val()
        var passWord = $('input[name = passWord]').val()
        myajax.post(
            {
                'url':'',
                'data':{
                    'email':email,
                    'passWord':passWord
                },
                'success':function (data){
                    console.log(data)
                },
                'fail':function (data) {
                    console.log(error)
                }
            }
        )
    })
})