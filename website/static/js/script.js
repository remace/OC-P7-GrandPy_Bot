let FORM = document.getElementById('form');
let INPUT = document.getElementById('question_textfield');
let BUTTON = document.getElementById('validate_button');


function send_data(){
    let myHeaders = new Headers();
    let myInit = {
        method: 'GET',
        headers: myHeaders,
        mode: 'cors',
        cache: 'default'
    };

    let params={
        'sentence': INPUT.value
    }
    
    fetch('http://127.0.0.1:5000/AskGrandPy/?sentence='+params.sentence)
        .then(res => res.json())
        .then(data => addNewDiv(data))
};

function addNewDiv(data){
    
}


BUTTON.addEventListener('click', function (event){
    send_data()
});

FORM.addEventListener('submit', function (event){
    send_data()
});