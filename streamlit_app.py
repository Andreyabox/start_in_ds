import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("data/df.csv")


def show_salary():
    fig, ax = plt.subplots()
    fig.set_figheight(7)
    fig.set_figwidth(15)
    plt.yticks(np.arange(1000, 150000, step=5000))
    plt.grid()
    plt.plot(df['Добыча полезных ископаемых'], color='green', marker='.', markersize=8)
    plt.plot(df['Обрабатывающие производства'], color='blue', marker='.', markersize=8)
    plt.plot(df['Производство кокса и нефтепродуктов'], color='red', marker='.', markersize=8)
    plt.title('График изменения зарплат, по отраслям, без учёта инфляции')
    plt.xlabel('Дата')
    plt.ylabel('Зарплата в рублях')
    plt.legend()
    st.pyplot(fig)
    st.write('По графику видно. Что в целом наблюдается рост зарплат по отраслям с 2000 года, кроме снижения зарплат в отрасле "Производство кокса и нефтепродуктов" в 2017 году, после опережающего роста зарплат по сравнению с другими отраслями.')

def show_inf():
    fig, ax = plt.subplots()
    fig.set_figheight(7)
    fig.set_figwidth(15)
    plt.grid()
    plt.plot(df['Прирост % Добыча полезных ископаемых'], color='green', marker='.', markersize=8)
    plt.plot(df['Прирост % Обрабатывающие производства'], color='blue', marker='.', markersize=8)
    plt.plot(df['Прирост % Производство кокса и нефтепродуктов'], color='red', marker='.', markersize=8)
    plt.plot(df['Годовая инфляция'], color='black', marker='.', markersize=8)
    plt.title('Влияние инфляции на рост зарплат')
    plt.xlabel('Дата')
    plt.ylabel('Зарплата в рублях')
    plt.legend(['Прирост % Добыча полезных ископаемых',
            'Прирост % Обрабатывающие производства',
            'Прирост % Производство кокса и нефтепродуктов',
            'Годовая инфляция'
           ])
    st.pyplot(fig)
    st.write('По графику видно, что рост зарплат в целом не на много опережает уровень инфляции')

def show_salary_inf():
    fig, ax = plt.subplots()
    fig.set_figheight(7)
    fig.set_figwidth(15)
    plt.grid()
    plt.plot(df['Добыча полезных ископаемых, с учётом инфляции'], color='green', marker='.', markersize=8)
    plt.plot(df['Обрабатывающие производства, с учётом инфляции'], color='blue', marker='.', markersize=8)
    plt.plot(df['Производство кокса и нефтепродуктов, с учётом инфляции'], color='red', marker='.', markersize=8)
    plt.title('График изменения зарплат, по отраслям, с учётом инфляции')
    plt.xlabel('Дата')
    plt.ylabel('Зарплата в рублях')
    plt.legend(df.loc[:,'Добыча полезных ископаемых, с учётом инфляции':])
    st.pyplot(fig)
    st.write('Как видим, зарплаты растут, даже если учитывать инфляцию')
  

def show_main_page():
    st.title("Проект: анализ зарплат в России")

    st.text("Заработные платы взяты с 2000 года по 2023")
    st.write('Для анализа были выраны 3 экономические деятельности:\n'
          +'1) Добыча полезных ископаемых;\n'
          +'2) Обрабатывающие производства;\n'
          +'3) Производство кокса и нефтепродуктов.')
    show_salary()
    st.header("Прирост зарплат в процентах и инфляция")
    show_inf()
    st.header("График зарплат с учётом инфляции")
    show_salary_inf()
    

if __name__ == "__main__":
    show_main_page()