# views.py

from django.http import JsonResponse
import pandas as pd
import joblib


from django.shortcuts import render
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer

from heart.forms import HeartForm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

heart_df = pd.read_csv('heart.csv')

# Преобразование категориальных данных
heart_df = pd.get_dummies(heart_df, columns=['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope'])

# Разделение на признаки и целевую переменную
X = heart_df.drop(['HeartDisease'], axis=1)
y = heart_df['HeartDisease']

# Сохраняем имена столбцов до применения импьютера
column_names = X.columns

# Создание и применение импьютера
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)

# Преобразование обратно в DataFrame
X = pd.DataFrame(X, columns=column_names)

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Обучение модели
# Импорты и подготовка данных...

# Обучение модели и расчет точности
heart_rf = RandomForestClassifier()
heart_rf.fit(X_train, y_train)
predictions = heart_rf.predict(X_test)
accuracy = accuracy_score(y_test, predictions) * 100  # Преобразование в проценты

def heart_home(request):
    heart_form = HeartForm(request.POST or None)
    diagnosis = ''

    if request.method == 'POST' and heart_form.is_valid():
        form_data = heart_form.cleaned_data
        user_input_dict = {
            'Age': form_data.get('age'),
            'RestingBP': form_data.get('resting_bp'),
            'Cholesterol': form_data.get('cholesterol'),
            'FastingBS': form_data.get('fasting_bs'),
            'MaxHR': form_data.get('max_hr'),
            'Oldpeak': form_data.get('oldpeak'),
            # Для категориальных данных используем one-hot encoding
            'Sex_M': 1 if form_data.get('sex') == 'M' else 0,
            'Sex_F': 1 if form_data.get('sex') == 'F' else 0,
            'ChestPainType_ATA': 1 if form_data.get('chest_pain_type') == 'ATA' else 0,
            'ChestPainType_NAP': 1 if form_data.get('chest_pain_type') == 'NAP' else 0,
            # Продолжите для всех категорий...
            'ExerciseAngina_Y': 1 if form_data.get('exercise_angina') == 'Y' else 0,
            'ExerciseAngina_N': 1 if form_data.get('exercise_angina') == 'N' else 0,
            'ST_Slope_Up': 1 if form_data.get('st_slope') == 'Up' else 0,
            'ST_Slope_Flat': 1 if form_data.get('st_slope') == 'Flat' else 0,

        }

        userdata = pd.DataFrame([user_input_dict])
        missing_cols = set(column_names) - set(userdata.columns)
        for col in missing_cols:
            userdata[col] = 0
        userdata = userdata.reindex(columns=column_names)

        # Применение импьютера и преобразование обратно в DataFrame
        userdata_transformed = imputer.transform(userdata)
        userdata = pd.DataFrame(userdata_transformed, columns=column_names)

        userresult = heart_rf.predict(userdata)
        diagnosis = 'Обнаружено сердечное заболевание' if userresult[0] == 1 else 'Сердечного заболевания не обнаружено'

    context = {
        'form': heart_form,
        'diagnosis': diagnosis,
        'accuracy': accuracy  # Передача сохраненного значения точности
    }

    return render(request, 'heart/home.html', context)



