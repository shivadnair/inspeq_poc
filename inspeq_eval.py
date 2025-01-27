# this script is basically evaluating the user prompts sent to the AI app
import inspeq_auth

inspeq_auth = inspeq_auth.inspeq_auth()

#function to evaluate the texts using inspeq
def inspeq_metric_eval(prompt, response = None, metrics_list=["RESPONSE_TONE", "ANSWER_RELEVANCE", "TOXICITY"]):
    if response:
        input_data = [
            {
                "prompt": prompt, 
                "response": response, 
                "context": "Provide a factual and relevant answer to the question."
            }
        ]
        task_name = "post_evaluation_task"
    else:
        input_data = [{"prompt": prompt}]
        task_name = "pre_evaluation_task"
    
    try:
        evaluation_results = inspeq_auth.evaluate_llm_task(
            metrics_list=metrics_list,
            input_data=input_data,
            task_name=task_name
        )
        return evaluation_results
    except Exception as e:
        print(f"Error during pre-evaluation: {e}")
        return None