# Education Patterns

Patterns for explanations, tutoring, curriculum design, and assessment creation.

## Table of Contents
- [Beginner Patterns](#beginner-patterns)
- [Intermediate Patterns](#intermediate-patterns)
- [Advanced Patterns](#advanced-patterns)

---

## Beginner Patterns

### ELI-X (Explain Like I'm X)

Adapt explanations to specific comprehension levels.

**Template:**
```
Explain [TOPIC] for [TARGET AUDIENCE].

Use:
- Simple language appropriate for their level
- Relatable analogies from their experience
- Concrete examples they would encounter
- Step-by-step breakdown where needed

Avoid:
- Jargon without definition
- Assumptions about prior knowledge
- Abstract concepts without grounding
```

**Examples:**
- "Explain a lunar eclipse for an 8-year-old using everyday objects they might see at home."
- "Explain covalent bonding as if I were a 10th grader who understands atoms but not molecular structures."
- "Explain Kubernetes to a senior executive who understands business but not infrastructure."

---

### Basic Quiz Generation

Create assessment questions with specified parameters.

**Template:**
```
Create [NUMBER] [QUESTION TYPE] questions on [TOPIC] for [GRADE LEVEL].

Parameters:
- Difficulty: [easy/medium/hard]
- Question types: [multiple choice / short answer / true-false]
- Focus areas: [specific subtopics]

Format each question as:
1. [Question]
   a) [Option A]
   b) [Option B]
   c) [Option C]
   d) [Option D]
   
   Correct Answer: [letter]
   Explanation: [why this is correct and others aren't]
```

---

### Concept Definition Generator

Create structured definitions with examples and connections.

**Template:**
```
Define [CONCEPT] for [GRADE LEVEL / AUDIENCE] in [SUBJECT AREA].

Include:
1. Clear, age-appropriate definition
2. 2-3 examples showing the concept in action
3. 1-2 non-examples (what it is NOT)
4. Connection to concepts they already know
5. A memorable analogy or mnemonic

Verify the explanation doesn't oversimplify to the point of inaccuracy.
```

**Example:**
```
Define "democracy" for 6th-grade social studies.

Include:
- Clear definition using 6th-grade vocabulary
- Historical example (ancient Athens) and modern example (US elections)
- Distinction from monarchy and dictatorship
- Connection to voting and representation (concepts they know)
- A memorable analogy comparing it to classroom decision-making
```

---

## Intermediate Patterns

### PARTS Framework Lesson Plan

Comprehensive lesson planning using Persona, Aim, Recipients, Theme, Structure.

**Template:**
```
Create a lesson plan using the PARTS framework:

PERSONA: You are an expert [SUBJECT] teacher
AIM: Students will be able to [LEARNING OBJECTIVE]
RECIPIENTS: [GRADE LEVEL] students who [PRIOR KNOWLEDGE/CHARACTERISTICS]
THEME: [TOPIC/CONCEPT]
STRUCTURE: [DURATION] lesson

LESSON PLAN:

1. WARM-UP ([X] minutes):
   - Activation activity connecting to prior knowledge

2. DIRECT INSTRUCTION ([X] minutes):
   - Key concepts with explanations
   - Visual aids or demonstrations

3. GUIDED PRACTICE ([X] minutes):
   - Structured activity with scaffolding
   - Check for understanding questions

4. INDEPENDENT PRACTICE ([X] minutes):
   - Student application of concepts
   - Differentiation options

5. ASSESSMENT:
   - How to check if objective is met
   - Exit ticket or formative assessment

6. DIFFERENTIATION:
   - Supports for struggling learners
   - Extensions for advanced learners

MATERIALS NEEDED: [list]
STANDARDS ALIGNMENT: [if applicable]
```

---

### Adaptive Difficulty Tutoring

Responsive tutoring that adjusts based on understanding.

**Template:**
```
You are a patient, encouraging tutor helping with [SUBJECT/TOPIC].

TUTORING APPROACH:
1. Begin by asking what specific aspect they need help with
2. Gauge understanding with 1-2 diagnostic questions
3. Identify any misconceptions

ADAPTATION RULES:
- If struggling: Break into smaller steps, provide hints, use simpler analogies
- If progressing: Increase complexity, ask probing questions
- If mastering: Challenge with application problems, ask them to teach it back

THROUGHOUT:
- Celebrate progress explicitly
- Never make them feel bad for not understanding
- Connect new concepts to what they already know

Start by asking: "What part of [topic] would you like to work on today?"
```

---

### Study Guide Creation

Generate leveled study materials aligned with objectives.

**Template:**
```
Create a study guide for [TOPIC] for [GRADE/COURSE]:

LEARNING OBJECTIVES:
- [Objective 1]
- [Objective 2]
- [Objective 3]

STUDY GUIDE SECTIONS:

1. KEY CONCEPTS (organized by importance):
   - Must know: [essential concepts]
   - Should know: [important but secondary]
   - Nice to know: [enrichment]

2. VOCABULARY:
   | Term | Definition | Example |
   |------|------------|---------|

3. COMMON MISCONCEPTIONS:
   - [Misconception]: [Correction]

4. PRACTICE QUESTIONS (by level):
   - Recall level: [questions testing memory]
   - Application level: [questions requiring use]
   - Analysis level: [questions requiring deeper thinking]

5. MEMORY AIDS:
   - Mnemonics, acronyms, visual organizers

6. STUDY TIPS:
   - Recommended study sequence
   - Self-testing strategies
```

---

## Advanced Patterns

### Socratic Dialogue Tutor

Implement authentic Socratic questioning that develops critical thinking.

**Template:**
```
You are a Socratic tutor. Your goal is to develop understanding through questioning, not direct answers.

RULES:
- NEVER provide direct answers
- Ask only ONE question at a time
- Wait for response before continuing

QUESTION TYPES TO USE:
1. Clarification: "What do you mean by...?" "Can you give an example?"
2. Assumption probing: "What are you assuming here?" "Why do you think that's true?"
3. Evidence seeking: "What evidence supports that?" "How do you know?"
4. Alternative viewpoints: "What might someone who disagrees say?" "Is there another way to look at this?"
5. Implication exploration: "If that's true, what follows?" "What are the consequences?"
6. Meta-questions: "Why do you think I asked that?" "What's the key question here?"

WHEN STUDENT IS STUCK:
- Rephrase the question more simply
- Offer a hint in question form: "What if you considered...?"
- Suggest they think about a related concept they understand

BEGIN with: "What's your current understanding of [topic]?"
```

**Model notes:**
- **Claude**: Has built-in "Learning Mode" with Socratic capabilities
- **GPT**: Needs explicit "do not break character" instructions
- **Gemini**: May need stronger guardrails to prevent direct answers

---

### Curriculum Design Assistant (Backward Design)

Apply Understanding by Design methodology.

**Template:**
```
Design curriculum for [COURSE/UNIT] using backward design:

STAGE 1: DESIRED RESULTS

Standards:
- [Standard 1]
- [Standard 2]

Enduring Understandings (big ideas that last):
- [Understanding 1]
- [Understanding 2]

Essential Questions (questions that recur and provoke inquiry):
- [Question 1]
- [Question 2]

Knowledge (students will know):
- [Fact/concept 1]
- [Fact/concept 2]

Skills (students will be able to):
- [Skill 1]
- [Skill 2]

STAGE 2: ASSESSMENT EVIDENCE

Performance Tasks (authentic application):
- [Task description with real-world context]

Other Evidence:
- Quizzes/tests: [what they assess]
- Observations: [what to look for]
- Work samples: [what to collect]

STAGE 3: LEARNING PLAN

Lesson Sequence:
1. [Lesson 1]: [objective, activities, assessment]
2. [Lesson 2]: [objective, activities, assessment]
... 

Instructional Strategies:
- [Strategy 1]: [when/why to use]

Differentiation:
- For struggling: [supports]
- For advanced: [extensions]

Resources:
- [Materials needed]
```

---

### Multi-Modal Educational Content

Generate coordinated content across formats.

**Template:**
```
Create multi-modal learning content for [TOPIC] for [AUDIENCE]:

1. VISUAL COMPONENT:
   Describe a diagram/infographic including:
   - Layout and structure
   - Key elements and labels
   - Color coding scheme
   - How elements relate visually

2. NARRATIVE TEXT:
   Write age-appropriate explanation:
   - Hook/attention grabber
   - Core concept explanation
   - Real-world connection
   - Summary/takeaway

3. AUDIO SCRIPT (for narration):
   - Conversational tone
   - Pace markers [pause], [emphasis]
   - Questions to prompt thinking
   - Duration target: [X] minutes

4. INTERACTIVE ELEMENT:
   Describe a learning activity:
   - Step-by-step instructions
   - Decision points for learner
   - Feedback for correct/incorrect
   - Extension challenge

5. HANDS-ON ACTIVITY:
   - Materials needed (accessible)
   - Procedure steps
   - Discussion questions
   - Assessment criteria

Ensure all modes reinforce the same core concepts and can stand alone or work together.
```

---

### Misconception Diagnosis and Remediation

Identify and address common misunderstandings.

**Template:**
```
Help diagnose and remediate misconceptions about [TOPIC]:

COMMON MISCONCEPTIONS IN THIS TOPIC:
1. [Misconception]: [Why students think this]
2. [Misconception]: [Why students think this]
3. [Misconception]: [Why students think this]

DIAGNOSTIC QUESTIONS:
Questions that reveal which misconception a student holds:
- [Question 1]: If they answer [X], they likely believe [misconception A]
- [Question 2]: If they answer [Y], they likely believe [misconception B]

REMEDIATION STRATEGIES:
For each misconception:
- Cognitive conflict: [activity that creates contradiction]
- Correct model: [accurate explanation]
- Practice: [exercises that reinforce correct understanding]
- Check: [how to verify misconception is resolved]

Start diagnosis by asking: "[Diagnostic question that reveals common misconceptions]"
```
