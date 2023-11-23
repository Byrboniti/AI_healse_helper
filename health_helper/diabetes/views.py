from django.shortcuts import render
from .forms import UserInputForm
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
import pandas as pd

# Загрузка и подготовка обучающего набора данных
df = pd.read_csv('diabetes.csv')
x = df.drop(['Outcome'], axis=1)
y = df['Outcome']

# Обучение модели
rf = RandomForestClassifier()
rf.fit(x, y)

# Создаем импьютер для заполнения NaN значений
# Здесь мы заполняем NaN средним значением столбца, но можно выбрать и другой метод
imputer = SimpleImputer(strategy='mean')
x = imputer.fit_transform(x)

# Загрузка точности модели (в вашем случае, вы можете обновлять ее при каждом вызове home, если это необходимо)
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=0)
rf.fit(xtrain, ytrain)
accuracy = accuracy_score(ytest, rf.predict(xtest)) * 100


def home(request):
    form = UserInputForm(request.POST or None)
    diagnosis = ''

    if request.method == 'POST' and form.is_valid():
        # Получаем данные из формы и преобразуем в словарь с правильными названиями столбцов
        form_data = form.cleaned_data
        user_input_dict = {
            'Pregnancies': form_data.get('pregnancies'),
            'Glucose': form_data.get('glucose'),
            'BloodPressure': form_data.get('blood_pressure'),
            'SkinThickness': form_data.get('skin_thickness'),
            'Insulin': form_data.get('insulin'),
            'BMI': form_data.get('bmi'),
            'DiabetesPedigreeFunction': form_data.get('diabetes_pedigree_function'),
            'Age': form_data.get('age')
        }

        # Создаем DataFrame для предсказания
        userdata = pd.DataFrame(user_input_dict, index=[0])

        # Заполнение NaN значений
        userdata = imputer.transform(userdata)

        userresult = rf.predict(userdata)
        diagnosis = 'Обнаружен диабет' if userresult[0] == 1 else 'Диабета не обнаружено'

    context = {
        'form': form,
        'accuracy': accuracy,
        'diagnosis': diagnosis,
    }

    return render(request, 'diabetes/home.html', context)
