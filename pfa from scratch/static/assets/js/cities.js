var state_arr = new Array("Tanger-Tétouan-Al Hoceïma", "L'Oriental", "Fès-Meknès", "Rabat-Salé-Kénitra", "Béni Mellal-Khénifra", "Casablanca-Settat", "Marrakech-Safi", "Drâa-Tafilalet", "Souss-Massa", "Guelmim-Oued Noun", "Laâyoune-Sakia El Hamra", "Dakhla-Oued Ed Dahab");

var s_a = new Array();
s_a[0]="";
s_a[1]="Tanger|Tétouan|Ksar El Kebir|Larache|Martil|Ouezzane|Al Hoceïma|Chefchaouene|Zoumi|Laouamra|Imzouren|Asilah|Taza|Tamorot";
s_a[2]="Oujda-Angad|Taourirt|Nador|Berkane|Guercif|Al Aaroui|Jerada|El Aïoun|Zaïo|Zeghanghane|Bou Arfa";
s_a[3]="Fès|Meknès|Taza|Sefrou|Azrou|Taounate|El Hajeb|Tahla|Missour|Oulad Tayeb";
s_a[4]="Rabat|Sale|Kenitra|Temara|Sidi Slimane|Tiflet|Sidi Qacem|Skhirate|Sidi Yahia El Gharb|Arbaoua|Mechraa Bel Ksiri|Mograne|Lalla Mimouna|Moulay Bousselham|Bouknadel|Safsaf";
s_a[5]="Béni Mellal|Khénifra|Al Fqih Ben salah|Oued Zem|Aguelmous|Dar Ould Zidouh|Ouaoula";
s_a[6]="Casablanca|Mohammedia|El Jadida|Settat|Bouskoura|Moulay Abdallah|Aïn Harrouda|Benslimane|Sidi Bennour|Azemmour|Bouznika|Mediouna|Bou Ahmed|Tit Mellil|Sidi Smai'il|Zawyat an Nwaçer";
s_a[7]="Marrakech|Safi|Essaouira|Youssoufia|Ait Ourir|Chichaoua";
s_a[8]="Errachidia|Tineghir|Zagora|Arfoud|Skoura";
s_a[9]="Agadir|Inezgane|Oulad Teïma|Taroudannt|Ait Ali|Tiznit|Aourir";
s_a[10]="Guelmim|Tan-Tan|Sidi ifni";
s_a[11]="smara|Laâyoune";
s_a[12]="Dakhla";

function print_state(state_id){
	// given the id of the <select> tag as function argument, it inserts <option> tags
	var option_str = document.getElementById(state_id);
	option_str.length=0;
	option_str.options[0] = new Option('Select State','');
	option_str.selectedIndex = 0;
	for (var i=0; i<state_arr.length; i++) {
		option_str.options[option_str.length] = new Option(state_arr[i],state_arr[i]);
	}
}

function print_city(city_id, city_index){
	var option_str = document.getElementById(city_id);
	option_str.length=0;	// Fixed by Julian Woods
	option_str.options[0] = new Option('Select City','');
	option_str.selectedIndex = 0;
	var city_arr = s_a[city_index].split("|");
	for (var i=0; i<city_arr.length; i++) {
		option_str.options[option_str.length] = new Option(city_arr[i],city_arr[i]);
	}
}
