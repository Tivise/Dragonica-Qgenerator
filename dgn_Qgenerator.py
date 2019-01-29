quest_id = input("Quelle est l'ID de la quête?")
group_quest_id = input("Quel est l'ID du groupe de quête?")
quest_name, quest_name_id = input("Quelle est le nom de la quête?"), input("l'id du nom de quête?")
quest_event = int(input("Quel type de quête faîtes-vous? 1: Parler, 2: Tuer mob, 3: Location, 4: Combo, 5: ZDM"))
if quest_event == 1:
    talk_deb, talk_deb_face = input("> Parler: Donnez le GUID du PNJ qui possède la quête"), input("Face_ID du NPC? (Exemple: Colin_normal)")
    talk_end, talk_end_face = input("> Parler: Donnez le GUID du PNJ qui doit être vu"), input("Face_ID du NPC? (Exemple: Colin_normal)")
    fichier = open('QUEST' + quest_id + '.xml', "a")
fichier.write('<?xml version="1.0" encoding="euc-kr"?>'
    '\n <!-- Quest Generator by PAZDER Thomas -->\n'
    f' <QUEST>\n <ID>{quest_id}</ID>\n'
    f'<GROUPNO>0</GROUPNO> \n <TITLE TEXT="{quest_name}"></TITLE>\n'
    f'<GROUPNAME TEXT="{group_quest_id}"></GROUPNAME>\n')
if quest_event == 1:
    talk_objectif_text, talk_objectif_id = input("Texte de l'objectif de quête"), input("ID de l'objectif de la quête")
    fichier.write(
    f'	<CLIENTS>\n<CLIENT TYPE="NPC" EVENTNO="10000">{talk_deb}</CLIENT>\n'
    f'</CLIENTS>\n <AGENTS> \n <AGENT TYPE="NPC" EVENTNO="10001">{talk_deb}</AGENT>\n'
    f'<AGENT TYPE="NPC" EVENTNO="10002" MARK="END">{talk_end}</AGENT>\n </AGENTS>\n <PAYERS>\n'
    f'<PAYER TYPE="NPC" EVENTNO="10003">{talk_end}</PAYER>\n </PAYERS>\n'
    '<EVENTS>\n <NPC OBJECTNO="0" TYPE="CLIENT" VALUE="101">10000</NPC>\n<NPC OBJECTNO="0" TYPE="ING_DLG" VALUE="501">10001</NPC>\n'
    '<NPC OBJECTNO="0" TYPE="ING_DLG" VALUE="601">10002</NPC>\n<NPC OBJECTNO="1" TYPE="INCPARAM" VALUE="601/1">10002</NPC>\n'
    '<NPC OBJECTNO="0" TYPE="PAYER" VALUE="601">10003</NPC>\n</EVENTS>\n'
    f'<OBJECTS TYPE="NOSTEP">\n<OBJECT1 COUNT="1" TEXT="{talk_objectif_id}"/>\n</OBJECTS>\n')
    talk_dialogue_debut, talk_dialogue_debut_id = input("Quel est le dialogue de début? (Que le PNJ de départ annonce)"), input("Quel est l'ID de ce message?")
    talk_dialogue_accept, talk_dialogue_accept_id = input("Quel est le dialogue lors de l'acceptation de la quête?"), input("Quel est l'ID de ce message?")
    talk_dialogue_encours, talk_dialogue_encours_id = input("Quel est le dialogue lorsque le joueur vient voir le premier PNJ, alors qu'il n'a pas accomplis la quête?"), input("Quel est l'ID de ce message?")
    talk_dialogue_confirm, talk_dialogue_confirm_id = input("Quel est le dialogue quand le joueur vient voir le PNJ?"), input("Quel est l'ID de ce message?")
    talk_questinfo_task, talk_questinfo_npcvalidation, talk_questinfo_details, talk_questinfo_id = input("Objectif? (Parlez à Bidule)"), input("Nom du PNJ"), input("Details...(infos additionnelles)"), input("ID du bloc d'information de quêtes?")

    fichier.write(f'<DIALOGS>\n<DIALOG ID="101" TYPE="PROLOG">\n<BODY TEXT="{talk_dialogue_debut_id}" FACE="{talk_deb_face}"/>\n<SELECT ID="10000" TYPE="ACCEPT" TEXT="500004"></SELECT>\n</DIALOG>\n'
	f'<DIALOG ID="301">\n<BODY TEXT="{talk_dialogue_accept_id}" FACE="{talk_deb_face}"/>\n<SELECT ID="0" TEXT="500003"></SELECT>\n</DIALOG>\n'
    f'<DIALOG ID="501">\n<BODY TEXT="{talk_dialogue_encours_id}" FACE="{talk_deb_face}"/>\n<SELECT ID="0" TEXT="500003"></SELECT>\n</DIALOG>\n'
	f'<DIALOG ID="552">\n<BODY TEXT="{talk_dialogue_confirm_id}" FACE="{talk_end_face}"/>\n<SELECT ID="0" TEXT="500003"></SELECT>\n</DIALOG>\n'
	f'<DIALOG ID="601" TYPE="COMPLETE">\n<BODY TEXT="{talk_dialogue_confirm_id}" FACE="{talk_end_face}"/>\n<SELECT ID="30999" TYPE="COMPLETE" TEXT="500007"></SELECT>\n</DIALOG>\n'
	'<DIALOG ID="701">\n<BODY TEXT="500017"/>\n<SELECT ID="0" TEXT="500003"></SELECT>\n</DIALOG>\n'
    '<DIALOG ID="801">\n<BODY TEXT="500018"/>\n<SELECT ID="0" TEXT="500003"></SELECT>\n</DIALOG>\n'
	f'<DIALOG ID="901" TYPE="INFO">\n<BODY TEXT="{talk_questinfo_task}"/>\n</DIALOG>\n'
	'<DIALOG ID="902">\n<BODY TEXT="502048"/>\n<SELECT ID="0" TEXT="500003"></SELECT>\n</DIALOG>\n'
	'<DIALOG ID="903">\n<BODY TEXT="501835"/>\n<SELECT ID="0" TEXT="500003"></SELECT>\n</DIALOG>\n'
    '</DIALOGS>\n</QUEST>')
fichier.close()
