from django import forms

class HeartForm(forms.Form):
    # Пример полей формы, соответствующих вашему датасету
    age = forms.IntegerField(label='Возраст', min_value=0)
    sex = forms.ChoiceField(label='Пол', choices=[('M', 'Мужчина'), ('F', 'Женщина')])
    chest_pain_type = forms.ChoiceField(label='Тип боли в груди', choices=[('ATA', 'ATA'), ('NAP', 'NAP'), ('TA', 'TA'), ('ASY', 'ASY')])
    resting_bp = forms.IntegerField(label='Артериальное давление в покое', min_value=0)
    cholesterol = forms.IntegerField(label='Холестерин', min_value=0)
    fasting_bs = forms.ChoiceField(label='Глюкоза натощак', choices=[(0, 'Нет'), (1, 'Да')])
    resting_ecg = forms.ChoiceField(label='ЭКГ в покое', choices=[('Normal', 'Нормальное'), ('ST', 'ST'), ('LVH', 'LVH')])
    max_hr = forms.IntegerField(label='Максимальный пульс', min_value=0)
    exercise_angina = forms.ChoiceField(label='Стенокардия от физической нагрузки', choices=[('N', 'Нет'), ('Y', 'Да')])
    oldpeak = forms.FloatField(label='ST депрессия', min_value=0.0)
    st_slope = forms.ChoiceField(label='Наклон ST', choices=[('Up', 'Вверх'), ('Flat', 'Плоский'), ('Down', 'Вниз')])
