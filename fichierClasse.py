#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 16:10:26 2018

@author: davidrey
"""

##### Projet informatique : Partition de musique 

class Note():
    """ 
    Définis la class note représentant la note de musique. 
    
    Elle prend en argument:
        -la hauteur de la note en string ('do', 'ré', 'mi', 'fa', 'sol', 'la' , 'si')
        -la durée en string ('noir', 'blanche', 'croche' ...) et 
        -l'octave en int (numéro repertoriant l'octave)
        -l'octave est défini par défaut à 3 (octave du la 440Hz)
        
    Exemple: le "la 440hz" est donné par la = Note('la' , 'noir' , 3 ). La durée de la note a été arbitrairement choisi sur noire.
    """
    ## mettre hauteur et duree en objet 
    def __init__(self, hauteur, duree, octave=3):      ## Initialisation des notes
        self.duree = duree   
        self.hauteur = hauteur
        self.octave = octave
    
    def __repr__(self):
        return """({0}|{1}|{2})  """.format(self.hauteur,self.octave,self.duree)
    

    ### changer ces méthodes: 
    #def change_ton(self,ton2):      
    #    """ Change la hauteur de la note. """
    #    self.hauteur = ton2

    
    
    #def change_duree(self,duree2):  
    #    """ Change la durée de la note. """
    #    self.duree = duree2

    ### 
    
    
    #### définir uen class note_avec_duree 
    ### définir toute les notes avec toutes les durée sous le format do1noir, 
    ### créer automatique toute les notes avec toute les durée sur tout les octave
    ### 
    
    
class Partition():
    """  
    Définis la classe partition.
    
    Elle prend en argument:
        - une liste de note (voir classe Note)  
        - une pulsation (un entier)
        
    Exemple: les premier notes de l'hymne à la joie sont donnée par: 
            si = Note('si', 'noir')
            do = Note('do', 'noir')
            re = Note('re', 'noir')
            la = Note('la', 'noir')
            sol = Note('sol', 'noir')
            siblanche = Note('si', 'blance')
            lacroche = Note('la', 'blanche')
            liste_de_note = [si,si,do,re,re,do,si,la,sol,sol,la,si,siblanche,lacroche,la]
            pulsation : 125
            Hymne_a_la_joie = Partition(liste de note , pulsation)
    """
    
    def __init__(self, liste_notes , pulsation):              ### initialisation de la classe partition
        if isinstance(liste_notes, list):  ## on verifie que c'est bien une liste de note
            self.liste_notes = liste_notes 
        if isinstance(pulsation, int ):  ## on vérifie que la pulsation est un entier
            self.pulsation = pulsation
        
    def __repr__(self):
        return """ pulsation: {0} 
    notes : {1}""".format(self.pulsation , self.liste_notes)
    
    def add_note(self,note):      
        """ Ajoute une note en dernière position de la liste """
        self.liste_notes.append(note)
    
    def insert_note(self,note,i):    
        """ Insert une note à la i-ième place """
        self.liste_notes.insert(i,note)
       # self.liste_notes
    
    def remove_note(self,i):               
        """ Retire la note de la liste_notes à la i-ième position """
        del self.liste_notes[i]
        #return self.liste_notes

    def changePulsation(self,Nouvel_Pulsation): 
        """ Change la pulsation """
        self.pulsation = Nouvel_Pulsation
        #return self.pulsation
 
    
    
    ###################### Ne fonctionne pas, doit être revu 
    def add_list_note(self, pos_indice , list_to_add ):
        """
        Insert la list_to_add en plaçant la première note de la liste à la pos_indice
        
        Exemple: pour rajouter [si , la , si ] après la deuxième position à la liste 
                [si , do , ré , mi , la ré ] -> Partition.add_list_note(2,list_to_add)
        """
        print(pos_indice)
        print(list_to_add)
        new_list = self.liste_notes[0:pos_indice] + list_to_add + self.liste_notes[pos_indice:]
        self.liste_notes = new_list
        return self.liste_notes
    
    ######objectif: générer un fichier son et générer un fichier latex 
    ###### scipy.io.wavfile.write