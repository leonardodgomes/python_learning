#----------------------------------------------------------------------------------------------------------------------------------
#                                                    Data Analysis Process
#----------------------------------------------------------------------------------------------------------------------------------

# https://careerfoundry.com/en/blog/data-analytics/the-data-analysis-process-step-by-step/

# Like any scientific discipline, data analysis follows a rigorous step-by-step process. Each stage requires different skills and
# know-how. To get meaningful insights, though, it’s important to understand the process as a whole. An underlying framework is
# invaluable for producing results that stand up to scrutiny.


#  |       STEP 1        |  ->  |      STEP 2      |  ->  |     STEP 3     |  ->  |      STEP 4      |  ->  | 	    STEP 5        |
#  | Define the Question |      | Collect the Data |      | Clean the Data |      | Analyze the Data |      | Visualize and Share |


# Here are the steps we’ll take you through:

#    1. Defining the question
#    2. Collecting the data
#    3. Cleaning the data
#    4. Analyzing the data
#    5. Sharing your results
#    6. Embracing failure
#    7. Summary


#----------------------------------------------------------------------------------------------------------------------------------
#    1. Defining the question
#----------------------------------------------------------------------------------------------------------------------------------

# The first step in any data analysis process is to define your objective. In data analytics jargon, this is sometimes called
# the » problem statement «.

# Start by asking:

#   Sales and Marketing
#    » What is the ideal length of time between initial prospect contact and first follow-up?
#    » Which sales rep collateral has the greatest and least impact on conversion?
#    » Which customer segments are most likely to promote us on social media?
#    » What are the ideal cross-sell and up-sell opportunities per product? Per customer segment?
#    » How can we optimize retail display per location?
#    » What is the best path to conversion based on each funnel stage?
#    » Which marketing initiatives will actually maximize return?
#    » Which prices can we increase, and by how much, and still retain customers?
#    » Outcomes: Deeper customer understanding, refined sales strategies, more conversions, higher ATV,
#      smarter outreach, better social proof, optimized funnels, increased profits.

#   Human Resources
#    » What do our employees value most at work? (You could even segment this into top 10% of performers; by department; 
#      by role, and so on.)
#    » What do our longest-tenured/best-performing employees have in common?
#    » What do employees who leave within 1-2 years have in common?
#    » How effective are our onboarding programs? Training programs?
#    » How can we spot a valuable employee at risk of leaving?
#    » What percentage of employees are disengaged from the organization and from their work?
#    » What combination of compensation and bonuses will most motivate performance?
#    » Outcomes: Attract and retain the best talent, maximize productivity and employee satisfaction, pinpoint recruitment 
#      efforts, reduce churn expenses.

#   Supply Chain
#    » Where are the biggest holdups in paperwork and procurement?
#    » What are the most significant causes of delay?
#    » Which inspection errors occur most frequently?
#    » How resilient is the chain to external forces? How can we prepare?
#    » What hidden inefficiencies can we find and correct?
#    » Can any steps be eliminated?
#    » What are the biggest opportunities for additional supply chain profits?
#    » How can we best protect margin when demand falls?
#    » Outcomes: Streamline logistics, optimize predictive planning, eliminate hidden costs, achieve big-picture 
#      profitability.

#   Business Strategy
#    » How can we reduce expenses by 10%?
#    » How can we leverage our analytics project to produce the most significant impact?
#    » How do we best combine innovation with performance sustainability?
#    » What are our biggest value-creation drivers?
#    » What are our five biggest areas for improvement?
#    » What are the biggest threats to growth and scalability?
#    » What should be our #1 focus right now? Next quarter? Next year?

#----------------------------------------------------------------------------------------------------------------------------------
#    2. Collecting the data
#----------------------------------------------------------------------------------------------------------------------------------

# A key part of this is determining which data you need. This might be:
#   » Quantitative  (numeric)     data, e.g. sales figures 
#   » Qualitative   (descriptive) data, such as customer reviews.

# All data fit into one of three categories: first-party, second-party, and third-party data.

#    1. First-Party data: 
#           First- Party data are data that you, or your company, have directly collected from customers. It might come in the form of transactional
#           tracking data or information from your company’s customer relationship management (CRM) system.
#           Whatever its source, first-party data is usually structured and organized in a clear, defined way.
#           Other sources of first-party data might include customer satisfaction surveys, focus groups, interviews,
#           or direct observation.

#    2. Second-Party data?
#           To enrich your analysis, you might want to secure a secondary data source. Second-party data is the first-party data
#           of other organizations. This might be available directly from the company or through a private marketplace. The main
#           benefit of second-party data is that they are usually structured, and although they will be less relevant than
#           first-party data, they also tend to be quite reliable. Examples of second-party data include website, app or social
#           media activity, like online purchase histories, or shipping data.

#    3. Third-Party data?
#           Third-party data is data that has been collected and aggregated from numerous sources by a third-party organization.
#           Often (though not always) third-party data contains a vast amount of unstructured data points (big data). Many
#           organizations collect big data to create industry reports or to conduct market research. The research and advisory firm
#           Gartner is a good real-world example of an organization that collects big data and sells it on to other companies.
#           Open data repositories and government portals are also sources of third-party data.


# Reading CSV Files-------------------------------------------------------------------------------------------------------------

#Import pandas library as pd
import pandas as pd
#Read the model.csv file
csv_file =  pd.read_csv('C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Work\\Python\\99_Leonardo\\00_Datasets\\data_model.csv', sep=';')

# Reading Excel Files-------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------------
#    2. Cleaning the data
#----------------------------------------------------------------------------------------------------------------------------------

