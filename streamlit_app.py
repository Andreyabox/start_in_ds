import streamlit as st
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
    st.write("Для производства кокса и нефтепродуктов наблюдается рост заработной платы до 2017 года. После 2017 года плата снижается и начинает расти только после 2020.")
    st.write("Для производства резиновых и пластмассовых изделий рост заработной платы продолжается все года.")
    st.write("Для рыболовства, рыбоводства заработная плата активно растет на протяжении всех лет. После 2014 года и 2021 года заработная плата начинает расти более активно.")
  

def show_main_page():
  st.title("Проект: анализ зарплат в России")

  st.text("Заработные платы взяты с 2000 года по 2023")
  st.write('Для анализа были выраны 3 экономические деятельности:\n'
          +'1) производство кокса и нефтепродуктов;\n'
          +'2) производство резиновых и пластмассовых изделий;\n'
          +'3) рыболовство, рыбоводство.')
  st.table(df)
  show_salary()
  st.header("Заработные платы с учетом инфляции")
  #show_inflation()
  #show_real_salory()
  st.header("Уровень счастья в России")
  #show_hpi()
  #show_all_correlation()



if __name__ == "__main__":
    show_main_page()