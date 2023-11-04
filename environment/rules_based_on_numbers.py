def RBOnNumbers ():
    """
        Los estados estarán representados por los seis tipos de emociones según Eckman
            0 : Felicidad
            1 : Triste
            2 : Miedo
            3 : Asco
            4 : Ira
            5 : Sorpresa

        Las acciones estarán representadas por las cinco categorias en el cuestionario
            0 : Aritmética
            1 : Proporciones
            2 : Geometría
            3 : Porcentajes
            4 : Tiempo-Velocidad

        Devuelve un Diccionario estrucutrado como:
        {
            emocion_numero:{
                    categoria_numero:[(0: incorrecto ó 1: correcto , valor_probabilidad)]

                    .
                    .
                    . \n
                    categoria_numero_n : [ ...
                },
            .
            .
            . \n
            emocion_numero_n : { ...
        }
    """

    return {
        #Felicidad
        0: {
            #Aritmetica
            0: (1, 0.80),     # Si un estudiante está feliz, la probabilidad de responder correctamente es del 80%.

            #Proporciones
            1: (1, 0.85),     # "Si un estudiante está feliz, la probabilidad de responder correctamente es del 85%."

            #Geometría
            2: (1, 0.90),     # "Si un estudiante está feliz, la probabilidad de responder correctamente es del 90%.",

            #Porcentajes
            3: (1, 0.85),     # "Si un estudiante está feliz, la probabilidad de responder correctamente es del 85%.",

            #Tiempo-Velocidad
            4: (1, 0.95),     # "Si un estudiante está feliz, la probabilidad de responder correctamente es del 95%.",
        },
        
        #Tristeza
        1: {
            0: (0, 0.70),     #"Si un estudiante está triste, la probabilidad de responder incorrectamente es del 70%.",
            1: (0, 0.75),     #"Si un estudiante está triste, la probabilidad de responder incorrectamente es del 75%.",
            2: (0, 0.75),     #"Si un estudiante está triste, la probabilidad de responder incorrectamente es del 75%.",
            3: (0, 0.80),     #"Si un estudiante está triste, la probabilidad de responder incorrectamente es del 80%.",
            4: (0, 0.80),     #"Si un estudiante está triste, la probabilidad de responder incorrectamente es del 80%.",
        },

        #Miedo
        2: {
            0: (0, 0.60),     # "Si un estudiante está asustado, la probabilidad de responder incorrectamente es del 60%.",
            1: (0, 0.65),     # "Si un estudiante está asustado, la probabilidad de responder incorrectamente es del 65%.",
            2: (0, 0.70),     # "Si un estudiante está asustado, la probabilidad de responder incorrectamente es del 70%.",
            3: (0, 0.75),     # "Si un estudiante está asustado, la probabilidad de responder incorrectamente es del 75%.",
            4: (0, 0.70),     # "Si un estudiante está asustado, la probabilidad de responder incorrectamente es del 70%.",
        },

        #Asco
        3: {
            0: (0, 0.75),     # "Si un estudiante siente asco, la probabilidad de responder incorrectamente es del 75%.",
            1: (0, 0.70),     # "Si un estudiante siente asco, la probabilidad de responder incorrectamente es del 70%.",
            2: (0, 0.80),     # "Si un estudiante siente asco, la probabilidad de responder incorrectamente es del 80%.",
            3: (0, 0.85),     # "Si un estudiante siente asco, la probabilidad de responder incorrectamente es del 85%.",
            4: (0, 0.80),     # "Si un estudiante siente asco, la probabilidad de responder incorrectamente es del 80%.",
        },

        #Ira
        4: {
            0: (0, 0.85),     # "Si un estudiante está enojado, la probabilidad de responder incorrectamente es del 85%.",
            1: (0, 0.80),     # "Si un estudiante está enojado, la probabilidad de responder incorrectamente es del 80%.",
            2: (0, 0.85),     # "Si un estudiante está enojado, la probabilidad de responder incorrectamente es del 85%.",
            3: (0, 0.90),     # "Si un estudiante está enojado, la probabilidad de responder incorrectamente es del 90%.",
            4: (0, 0.90),     # "Si un estudiante está enojado, la probabilidad de responder incorrectamente es del 90%.",
        },

        #Sorpresa
        5: {
            0: (1, 0.75),     # "Si un estudiante está sorprendido, la probabilidad de responder correctamente es del 75%.",
            1: (1, 0.70),     # "Si un estudiante está sorprendido, la probabilidad de responder correctamente es del 70%.",
            2: (1, 0.80),     # "Si un estudiante está sorprendido, la probabilidad de responder correctamente es del 80%.",
            3: (1, 0.90),     # "Si un estudiante está sorprendido, la probabilidad de responder correctamente es del 90%.",
            4: (1, 0.85),     # "Si un estudiante está sorprendido, la probabilidad de responder correctamente es del 85%.",
        },
    }