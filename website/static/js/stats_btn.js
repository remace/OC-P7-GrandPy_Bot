const stats_toggle = document.getElementById('stats_toggle');
const stats_result = document.getElementById('stats_result')


stats_toggle.addEventListener('click', () =>{
    stats_toggle.classList.toggle('active')
    if (stats_toggle.classList.contains('active')){
        fetch('/stats')
            .then(res => res.json())
            .then(data => printTable(data))
        }
    else{
        stats_result.innerHTML = ''
    }
})

function printTable(data){
    let tbl = document.createElement("table")
    let tblhead = document.createElement("thead")
    let row = document.createElement("tr")
    let cell = document.createElement("th")
    cell.innerHTML = "région"
    row.appendChild(cell)
    cell = document.createElement("th")
    cell.innerHTML = "requêtes"
    row.appendChild(cell)
    tblhead.appendChild(row)
    tbl.appendChild(tblhead)
    
    
    let tblBody = document.createElement("tbody")
    
    for (let regionName in data){
        let value = data[regionName]
        row = document.createElement("tr")
        td = document.createElement('td')
        td.innerHTML= regionName
        row.appendChild(td)
        td = document.createElement('td')
        td.innerHTML = value.toString()
        row.appendChild(td)
        tblBody.appendChild(row)
    }


    tbl.appendChild(tblBody)
    stats_result.appendChild(tbl)
}