let data = [
    { item: 'Thiruvananthapuram',
     subitems: ['Venganoor','Vizhinjam','Vattiyoorkavu','Kovalam']
     },
    { item: 'Thrissur',
    subitems: ['Chavakkad', 'Guruvayoor', 'karalam', 'Kattoor']
    },
    { item: 'kollam',
     subitems:  ['Chavara','Chadayamangalam','kottiyoor','paravoor']
     },
    {item: 'pathanamthitta',
    subitems:['Adoor','Konni','Ranni','Pandalam']
     },
    {item: 'Alappuzha',
    subitems:['Aroor','Cherthala','Haripad','kalavoor'] },
  ];


  window.onload = function() {
  var itemSel = document.getElementById("district");
  var subitemSel = document.getElementById("branch");

  for (var x in data) {
    z=data[x].item
    itemSel.options[itemSel.options.length] = new Option(z,x);
  }
  itemSel.onchange = function() {
  //empty
  subitemSel.length = 1;
    //display correct values
    for (var y of data[this.value].subitems) {
      subitemSel.options[subitemSel.options.length] = new Option(y, y);
    }
  }
}