        INP
        STA X

        LDA ZERO
        STA CONT

LOOP    LDA CONT
        OUT

        SUB X
        BRZ FIM

        LDA CONT
        ADD UM
        STA CONT

        BRA LOOP

FIM     HLT

X       DAT 0
CONT    DAT 0
ZERO    DAT 0
UM      DAT 1
