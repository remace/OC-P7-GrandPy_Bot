let FORM = document.getElementById('form');
let INPUT = document.getElementById('question_textfield');
let BUTTON = document.getElementById('validate_button');
let ANSWER_CONTAINER = document.getElementById('answer_container')

console.log("connais tu le palais idéal du facteur cheval?")


BUTTON.addEventListener('click', function (event){
    send_data()
});

FORM.addEventListener('submit', function (event){
    send_data()
});

function send_data(){

    let params={
        'sentence': INPUT.value
    }
    
    fetch('http://127.0.0.1:5000/AskGrandPy/?sentence='+params.sentence)
        .then(res => res.json())
        .then(data => addNewDiv(data))
};

function addNewDiv(data){
    console.log(data)
    
    let gmaps_div =  create_google_maps_div(data)
    gmaps_div.classList.add('google_maps_container')
    
    let wikipedia_div  = create_wiki_div(data)
    wikipedia_div.classList.add('wikimedia_container')

    let answer = document.createElement('div', { class:'answer'})
    answer.classList.add('answer')
    answer.appendChild(gmaps_div)
    answer.appendChild(wikipedia_div)

    ANSWER_CONTAINER.appendChild(answer)
    
}

function create_google_maps_div(data){
    let div = document.createElement('div')
    let title = "gmaps_answer"
    let latitude = data.maps_info.results.geometry.location.lat
    let longitude = data.maps_info.results.geometry.location.lng
    let content = "<h3>"+title+"</h3><p>lat: "+latitude+"</p><p>lng:"+longitude+"</p>"
    div.innerHTML = content
    return (div)
}

function create_wiki_div(data){
    let div = document.createElement('div')
    let title = data.wiki_info.title
    let extract = data.wiki_info.intro
    let content = "<h3>"+title+"</h3><p>"+extract+"</p>"
    div.innerHTML = content   
    return (div)
}