from django import forms

class UserInputForm(forms.Form):
    PREGNANCIES_CHOICES = [(i, str(i)) for i in range(11)]
    GLUCOSE_CHOICES = [(i, str(i)) for i in range(201)]
    BP_CHOICES = [(i, str(i)) for i in range(123)]
    SKIN_THICKNESS_CHOICES = [(i, str(i)) for i in range(101)]
    INSULIN_CHOICES = [(i, str(i)) for i in range(847)]
    BMI_CHOICES = [(i, str(i)) for i in range(68)]
    DPF_CHOICES = [(round(i * 0.1, 1), str(round(i * 0.1, 1))) for i in range(25)]
    AGE_CHOICES = [(i, str(i)) for i in range(21, 89)]

    pregnancies = forms.ChoiceField(choices=PREGNANCIES_CHOICES, label='Перенесённых беременностей')
    glucose = forms.ChoiceField(choices=GLUCOSE_CHOICES, label='Уровень глюкозы')
    bp = forms.ChoiceField(choices=BP_CHOICES, label='Давление')
    skinthickness = forms.ChoiceField(choices=SKIN_THICKNESS_CHOICES, label='Толщина кожи')
    insulin = forms.ChoiceField(choices=INSULIN_CHOICES, label='Уровень инсулина')
    bmi = forms.ChoiceField(choices=BMI_CHOICES, label='Индекс массы тела')
    dpf = forms.ChoiceField(choices=DPF_CHOICES, label='Наследственность')
    age = forms.ChoiceField(choices=AGE_CHOICES, label='Возраст')
