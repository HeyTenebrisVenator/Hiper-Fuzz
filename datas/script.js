function url_collect() {

    input_with_url = document.getElementById('URL').value
    var request = new XMLHttpRequest(); 
    request.onreadystatechange = function() {
            if (request.readyState === XMLHttpRequest.DONE) {
                if (this.readyState == 4 && request.status === 200) {
                    if (request.responseText != 0) {
                        document.getElementById('Data_received').innerHTML = '<p>OK, CODE RECEIVED:</p><p class="code_'+ request.responseText +'">' + request.responseText + '</p>';
                        document.getElementById('url_collected').value = input_with_url
                        document.getElementById('all').style.display = 'inline'
                    }
                    else {
                        document.getElementById('Data_received').innerHTML = 'ERROR';
                        document.getElementById('all').style.display = 'none'                        
                    }
                }
                else {
                    document.getElementById('Data_received').innerHTML = 'ERROR';
                    document.getElementById('all').style.display = 'none'
                }
        }
    }
    request.open('GET', "http://127.0.0.1:4444/api?url=" + input_with_url, true);
    request.send();
}
function fuzz() {
    URL_TO_BE_SEND = document.getElementById('url_collected').value
    WORDLIST_TO_BE_SEND = document.getElementById('wordlist').value
    cookie = document.getElementById('cookie').value
    rate = document.getElementById('rate').value
    header = document.getElementById('header').value
    output = document.getElementById('output').value
    if (URL_TO_BE_SEND != '' && WORDLIST_TO_BE_SEND != '') {
        var request = new XMLHttpRequest(); 
        request.onreadystatechange = function() {
                if (request.readyState === XMLHttpRequest.DONE) {
                    if (this.readyState == 4 && request.status === 200) {
                        document.getElementById('completed').innerHTML = 'SENT!';
                    }
                    else {
                        document.getElementById('completed').innerHTML = 'ERROR';
                    }
            }
        }
        request.open('GET', "http://127.0.0.1:4444/api?complete_url=" + URL_TO_BE_SEND + '&wordlist=' + WORDLIST_TO_BE_SEND + '&cookies=' + cookie + '&rate=' + rate + '&header=' + header + '&output' + output, true);
        request.send();
    }
    else {
        document.getElementById('completed').innerHTML = 'PLEASE, SELECT THE WORDLIST';
    }


}