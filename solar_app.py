import streamlit as st
import pickle

log_model=pickle.load(open('log_model.pkl','rb'))

def classify(num):
    if num==0:
        return 'Yes the person is willing to buy solar'
    elif num==1:
        return 'Maybe the person will buy maybe not'
    else:
        return 'No the person wont buy solar'
def main():
    st.title("Prediction of Willingness to buy solar")
    # html_temp = """
    # <div style="background-color:teal ;padding:10px">
    # <h2 style="color:white;text-align:center;">SOLAR</h2>
    # </div>
    # """
    # st.markdown(html_temp, unsafe_allow_html=True)
    Level_of_education=['Never attended school','Up to class 5','Up to class 8','Up to class 12','Bachelor’s degree and above']
    option1=st.selectbox('Level of education:',Level_of_education)
    Satisfaction_with_power_availability=['very satisfied','satisfied','Neutral','unsatisfied','very unsatisfied']
    option2=st.selectbox('satisfaction with power availability:',Satisfaction_with_power_availability)
    Satisfaction_with_maintenance_support=['very satisfied','satisfied','Neutral','unsatisfied','very unsatisfied']
    option3=st.selectbox('Satisfaction with maintenance support:',Satisfaction_with_maintenance_support)
    Availability_of_parts_in_local_shop=['not available','Available in nearby village','Made available by service provider']
    option4=st.selectbox('Availability of parts in local shop:',Availability_of_parts_in_local_shop)
    Time_taken_for_repair=['Solved by self','0-2 weeks','3-5 weeks','Not solved yet']
    option5=st.selectbox('Time taken for repair:',Time_taken_for_repair)
    Duration_of_PV_system_use=['Up to 1 year','1-3 years','3-5 years','More than 5 years']
    option6=st.selectbox('Duration of PV system use:',Duration_of_PV_system_use)
    Operational_status_of_PV_system=['Working without faults','Working with minor faults','Working with major faults','Not working']
    option7=st.selectbox('Operational status of PV system:',Operational_status_of_PV_system)
    satisfaction_with_battery_life=['very satisfied','satisfied','Neutral','unsatisfied','very unsatisfied']
    option8=st.selectbox('satisfaction with battery life:',satisfaction_with_battery_life)
    o1=Level_of_education.index(str(option1))
    o2=Satisfaction_with_power_availability.index(str(option2))
    o3=Satisfaction_with_maintenance_support.index(str(option3))
    o4=Availability_of_parts_in_local_shop.index(str(option4))
    o5=Time_taken_for_repair.index(str(option5))
    o6=Duration_of_PV_system_use.index(str(option6))
    o7=Operational_status_of_PV_system.index(str(option7))
    o8=satisfaction_with_battery_life.index(str(option8))
    inputs=[[o1,o2,o3,o4,o5,o6,o7,o8]]
    if st.button('Predict'):
        st.success(classify(log_model.predict(inputs)))
        # elif option=='Logistic Regression':
        #     st.success(classify(log_model.predict(inputs)))
        # else:
        #    st.success(classify(svm.predict(inputs)))
if __name__=='__main__':
    main()
