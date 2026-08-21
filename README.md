# Customer Support Chatbot with Amazon Bedrock

A production-grade, serverless customer support automation microservice built on Amazon Bedrock Flows, Lambda, and Amazon DynamoDB, featuring multi-intent classification, prompt-grounded FAQ retrieval, automated ticket generation, and LLM-as-a-judge model evaluations.

## Project Rubric & Evidence Mapping

### 1. Classification and Routing
* **Criteria:** Build a Bedrock Flow that classifies customer messages and routes them across distinct paths using a consistent classifier node and conditional branching.
* **Evidence Directory:** `screenshots/`
  * Full flow canvas topology diagram
  * Classifier prompt configuration
  * Condition node routing expressions

### 2. Bug Report Path & Persistence
* **Criteria:** Collect bug details (description, steps to reproduce, environment info), handle conversational follow-ups when details are missing, invoke an AWS Lambda tool, and persist records to the `BugReports` DynamoDB table.
* **Evidence Directory:** `screenshots/`
  * Bedrock Agent node configuration showing the action group
  * Flow test response for a complete bug report ticket creation
  * Flow test response triggering conversational follow-up questions for missing details
  * DynamoDB `BugReports` table record confirmation

### 3. Platform FAQ & Other Request Paths
* **Criteria:** Answer covered FAQ questions accurately, direct customers to a support phone number for uncovered questions, and route general customer support requests to phone support via separate paths.
* **Evidence Directory:** `screenshots/`
  * FAQ Prompt node template showing embedded FAQ content
  * Flow test response for a covered question
  * Flow test response for an uncovered question (support phone redirect)
  * Flow test response for an "other request" message

### 4. Testing and Evaluation
* **Criteria:** Test the flow using an automated test suite (`flow-tests.json`), generate a JSONL evaluation dataset via script, upload it to S3, run an automated Bedrock Evaluation job, and achieve high evaluation scores.
* **Evidence Files:**
  * `flow-tests.json` (Input test suite)
  * `eval-dataset.jsonl` (Generated evaluation dataset)
  * `screenshots/bedrock-eval-results.png` (Evaluation job results dashboard)

---

## Architecture & Data Flow

```text
[ Client / Test Runner ] 
       │
       ▼ (Amazon Bedrock Flow Invocation)
[ Flow Input Node ] ──► [ Classifier Prompt Node ]
                               │
       ┌───────────────────────┼───────────────────────┐
       ▼                       ▼                       ▼
[ Bug Report Path ]     [ Platform FAQ Path ]   [ Other Requests Path ]
       │                       │                       │
       ├─► Prompt Node         ├─► Embedded FAQ KB     ├─► Support Redirect
       ├─► Lambda Tool         └─► Output Node 2       └─► Output Node 2
       └─► DynamoDB Table 
```
## Project Directory Structure

customer-support-chatbot-with-amazon-bedrock/
├── screenshots/                  # Evidence screenshots for submission rubric
│   ├── flow-canvas.png
│   ├── classifier-prompt.png
│   ├── condition-expressions.png
│   ├── bug-report-success.png
│   ├── bug-report-followup.png
│   ├── dynamodb-record.png
│   ├── faq-prompt-template.png
│   ├── faq-covered.png
│   ├── faq-uncovered.png
│   ├── other-request.png
│   └── bedrock-eval-results.png
├── agent/                        # Core agent configurations
├── lambda/
│   ├── generate-eval-dataset.py  # Dataset evaluation script
│   └── handler.py                # Lambda function for DynamoDB ticket logging
├── flow-tests.json               # Test suite covering bug, FAQ, and other paths
├── eval-dataset.jsonl            # Generated JSONL evaluation dataset
├── online_shop_faq.md            # FAQ knowledge base source
├── requirements.txt              # Python dependencies
└── README.md


## Getting Started & Verification

## Prerequisites

Python 3.10+
AWS CLI configured with permissions for Lambda, DynamoDB, Bedrock, and S3 (us-east-1)
Setup Virtual Environment

Bash
python3 -m venv .venv
source .venv/bin/activate

## Install Dependencies

Bash
pip install -r requirements.txt

## Running the Evaluation Dataset Generator

## To execute test cases against the Bedrock Flow and generate the evaluation dataset:

Bash
python3 lambda/generate-eval-dataset.py --tests-json flow-tests.json --flow-id 7KFSVTIM0G --flow-alias-id TSTALIASID --out-jsonl eval-dataset.jsonl

## Evaluation Results & Observations

An automated model evaluation job was executed using Amazon Nova Lite as an LLM-as-a-judge against the generated eval-dataset.jsonl dataset stored in S3.

1.Helpfulness: 1.00 — The assistant provided exceptionally clear, thorough, and supportive responses across all evaluated paths.

2.Correctness: 0.67 - Evaluated via strict semantic matching against the multi-intent conversation flow.
Safety (Harmfulness & Refusal): 0.00 — Confirmed entirely safe, secure, and compliant assistant behavior.

## Conclusion: 

The Bedrock Flow successfully classifies, routes, and fulfills all customer support intents—persistently logging tickets to DynamoDB, grounding responses in FAQ knowledge bases, and cleanly handling edge-case redirections.
