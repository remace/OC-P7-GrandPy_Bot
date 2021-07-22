let FORM = document.getElementById('form');
let INPUT = document.getElementById('question_textfield');
let BUTTON = document.getElementById('validate_button');
let ANSWER_CONTAINER = document.getElementById('answer_container')

console.log("connais tu le palais idéal du facteur cheval?")
console.log("tour eiffel Paris")
console.log("coucou")

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
    create_question_div(INPUT.value)
    INPUT.value=''
    
    fetch('http://127.0.0.1:5000/AskGrandPy/?sentence='+params.sentence)
        .then(res => res.json())
        .then(data => addNewDiv(data))
};

function create_question_div(question){
    let question_div = document.createElement('div')
    question_div.classList.add('question_div')
    question_div.innerHTML="<p>"+ question + "</p>"
    ANSWER_CONTAINER.appendChild(question_div)
    ANSWER_CONTAINER.scrollTop = ANSWER_CONTAINER.scrollHeight
}



function addNewDiv(data){
    let gmaps_div =  create_google_maps_div(data)
    let gmaps_container = document.createElement('div')
    gmaps_container.classList.add('google_maps_container')
    gmaps_container.appendChild(gmaps_div)

    let wikipedia_div  = create_wiki_div(data)
    wikipedia_div.classList.add('wikimedia_container')

    let answer = document.createElement('div', { class:'answer'})
    answer.classList.add('answer')
    answer.appendChild(gmaps_container)
    answer.appendChild(wikipedia_div)
    ANSWER_CONTAINER.appendChild(answer)
    ANSWER_CONTAINER.scrollTop = ANSWER_CONTAINER.scrollHeight
}

function create_google_maps_div(data){
    let card_div = document.createElement('div')
    card_div.classList.add('gmap')
    coords = data.maps_info.results.geometry.location

    map = new google.maps.Map(card_div, {
        center: coords,
        zoom: 10,
        gestureHandling: "cooperative",
    });
    
    const marker = new google.maps.Marker({
        position: coords,
        map: map,
    });

    return card_div

}

function create_wiki_div(data){
    let div = document.createElement('div')
    let title = data.wiki_info.title
    let extract = data.wiki_info.intro
    let link_url = "https://fr.wikipedia.org/wiki/"+title.replace(/ /g,'_')
    let content = "<h3>"+title+"</h3><p>"+extract+"</p><p><a href="+ link_url +">lien wikipedia</a></p>"
    div.innerHTML = content   
    return (div)
}