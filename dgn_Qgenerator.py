import os
tableau_id = {}
continuer = True
compteur = -1
while continuer:
    compteur += 1
    if compteur != 0:
        for key, value in tableau_id.items():
            tableau_id[key] += 1
    if compteur == 0:
        tableau_id['quest_id'] = int(input("Quelle est l'ID de la quête?"))
    quest_id = str(tableau_id['quest_id'])
    group_quest_id = int(input("Quel est l'ID du groupe de quête?"))
    quest_name = input("Quelle est le nom de la quête?")
    if compteur == 0:
        tableau_id['quest_name_id'] = int(input("l'id du nom de quête?"))
    quest_name_id = int(tableau_id['quest_name_id'])
    quest_event = int(input("Quel type de quête faîtes-vous? 1: Parler, 2: Tuer mob, 3: Location, 4: Combo, 5: ZDM"))
    fichier = open('QUEST' + quest_id + '.xml', "a", encoding='utf-8')
    fichier.write('<?xml version="1.0" encoding="euc-kr"?>'
    '\n <!-- Quest Generator by PAZDER Thomas(Tivise) -->\n'
    f' <QUEST>\n <ID>{quest_id}</ID>\n'
    f'<GROUPNO>0</GROUPNO> \n <TITLE TEXT="{quest_name_id}"></TITLE>\n'
    f'<GROUPNAME TEXT="{group_quest_id}"></GROUPNAME>\n')
    if quest_event == 1:
        talk_deb, talk_deb_face = input("> Parler: Donnez le GUID du PNJ qui possède la quête"), input(
        "Face_ID du NPC? (Exemple: Colin_normal)")
        talk_end, talk_end_face = input("> Parler: Donnez le GUID du PNJ qui doit être vu"), input(
        "Face_ID du NPC? (Exemple: Colin_normal)")
        talk_objectif_text = input("Texte de l'objectif de quête")
        if compteur == 0:
            tableau_id['talk_objectif_id'] = int(input("ID de l'objectif de la quête"))
        talk_objectif_id = int(tableau_id['talk_objectif_id'])
        fichier.write(
        f'	<CLIENTS>\n<CLIENT TYPE="NPC" EVENTNO="10000">{talk_deb}</CLIENT>\n'
        f'</CLIENTS>\n <AGENTS> \n <AGENT TYPE="NPC" EVENTNO="10001">{talk_deb}</AGENT>\n'
        f'<AGENT TYPE="NPC" EVENTNO="10002" MARK="END">{talk_end}</AGENT>\n </AGENTS>\n <PAYERS>\n'
        f'<PAYER TYPE="NPC" EVENTNO="10003">{talk_end}</PAYER>\n </PAYERS>\n'
        '<EVENTS>\n <NPC OBJECTNO="0" TYPE="CLIENT" VALUE="101">10000</NPC>\n<NPC OBJECTNO="0" TYPE="ING_DLG" VALUE="501">10001</NPC>\n'
        '<NPC OBJECTNO="0" TYPE="ING_DLG" VALUE="601">10002</NPC>\n<NPC OBJECTNO="1" TYPE="INCPARAM" VALUE="601/1">10002</NPC>\n'
        '<NPC OBJECTNO="0" TYPE="PAYER" VALUE="601">10003</NPC>\n</EVENTS>\n'
        f'<OBJECTS TYPE="NOSTEP">\n<OBJECT1 COUNT="1" TEXT="{talk_objectif_id}"/>\n</OBJECTS>\n')
        talk_dialogue_debut = input("Quel est le dialogue de début? (Que le PNJ de départ annonce)")
        if compteur == 0:
            tableau_id['talk_dialogue_debut_id'] = int(input("Quel est l'ID de ce message?"))
        talk_dialogue_debut_id = int(tableau_id['talk_dialogue_debut_id'])
        talk_dialogue_accept = input("Quel est le dialogue lors de l'acceptation de la quête?")
        if compteur == 0:
            tableau_id['talk_dialogue_accept_id'] = int(input("Quel est l'ID de ce message?"))
        talk_dialogue_accept_id = int(tableau_id['talk_dialogue_accept_id'])
        talk_dialogue_encours = input("Quel est le dialogue lorsque le joueur vient voir le premier PNJ, alors qu'il n'a pas accomplis la quête?")
        if compteur == 0:
            tableau_id['talk_dialogue_encours_id'] = int(input("Quel est l'ID de ce message?"))
        talk_dialogue_encours_id = int(tableau_id['talk_dialogue_encours_id'])
        talk_dialogue_confirm = input("Quel est le dialogue quand le joueur vient voir le PNJ?")
        if compteur == 0:
            tableau_id['talk_dialogue_confirm_id'] = int(input("Quel est l'ID de ce message?"))
        talk_dialogue_confirm_id = int(tableau_id['talk_dialogue_confirm_id'])
        talk_questinfo_task = input("Objectif? (Parlez à qui?)")
        talk_questinfo_npcvalidation = input("Nom du PNJ de validation")
        talk_questinfo_details = input("Details...(infos additionnelles)")
        if compteur == 0:
            tableau_id['talk_questinfo_id'] = int(input("ID du bloc d'information de quêtes?"))
        talk_questinfo_id = int(tableau_id['talk_questinfo_id'])
        fichier.write(f'<DIALOGS>\n<DIALOG ID="101" TYPE="PROLOG">\n<BODY TEXT="{talk_dialogue_debut_id}" FACE="{talk_deb_face}"/>\n<SELECT ID="10000" TYPE="ACCEPT" TEXT="500004"></SELECT>\n</DIALOG>\n'
        f'<DIALOG ID="301">\n<BODY TEXT="{talk_dialogue_accept_id}" FACE="{talk_deb_face}"/>\n<SELECT ID="0" TEXT="500003"></SELECT>\n</DIALOG>\n'
        f'<DIALOG ID="501">\n<BODY TEXT="{talk_dialogue_encours_id}" FACE="{talk_deb_face}"/>\n<SELECT ID="0" TEXT="500003"></SELECT>\n</DIALOG>\n'
        f'<DIALOG ID="552">\n<BODY TEXT="{talk_dialogue_confirm_id}" FACE="{talk_end_face}"/>\n<SELECT ID="0" TEXT="500003"></SELECT>\n</DIALOG>\n'
        f'<DIALOG ID="601" TYPE="COMPLETE">\n<BODY TEXT="{talk_dialogue_confirm_id}" FACE="{talk_end_face}"/>\n<SELECT ID="30999" TYPE="COMPLETE" TEXT="500007"></SELECT>\n</DIALOG>\n'
        '<DIALOG ID="701">\n<BODY TEXT="500017"/>\n<SELECT ID="0" TEXT="500003"></SELECT>\n</DIALOG>\n'
        '<DIALOG ID="801">\n<BODY TEXT="500018"/>\n<SELECT ID="0" TEXT="500003"></SELECT>\n</DIALOG>\n'
        f'<DIALOG ID="901" TYPE="INFO">\n<BODY TEXT="{talk_questinfo_id}"/>\n</DIALOG>\n'
        '<DIALOG ID="902">\n<BODY TEXT="502048"/>\n<SELECT ID="0" TEXT="500003"></SELECT>\n</DIALOG>\n'
        '<DIALOG ID="903">\n<BODY TEXT="501835"/>\n<SELECT ID="0" TEXT="500003"></SELECT>\n</DIALOG>\n'
        '</DIALOGS>\n</QUEST>')
        fichier.close()
        fichier_texte = open('questtexttable.xml', "a", encoding='utf-8')
        fichier_texte.write(f'<TEXT ID="{quest_name_id}" Text="{quest_name}"/>\n'
                            f'<TEXT ID="{talk_objectif_id}" Text="{talk_objectif_text}"/>\n'
                            f'<TEXT ID="{talk_dialogue_debut_id}" Text="{talk_dialogue_debut}"/>\n'
                            f'<TEXT ID="{talk_dialogue_accept_id}" Text="{talk_dialogue_accept}"/>\n'
                            f'<TEXT ID="{talk_dialogue_encours_id}" Text="{talk_dialogue_encours}"/>\n'
                            f'<TEXT ID="{talk_dialogue_confirm_id}" Text="{talk_dialogue_confirm}"/>\n'
                            f'<TEXT ID="{talk_questinfo_id}" Text="[Tâche de quête]\n{talk_questinfo_task}\n\n[PNJ de validation]\n{talk_questinfo_npcvalidation}\n\n[Détails]\n{talk_questinfo_details}"/>\n')
        fichier_texte.close()
    print(tableau_id)
    decision = input("Souhaitez-vous continuer la creation de quêtes? (les ids seront: ids+1)")
    while decision != "1" and decision != "0":
        decision = input("Souhaitez-vous continuer la creation de quêtes? (les ids seront: ids+1)")
    if int(decision) == 0:
        continuer = False
