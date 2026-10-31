from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.pagesizes import landscape
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import os, math

OUT='AI_101_Introduction_to_Artificial_Intelligence_Orientation.pdf'
W,H=13.333*inch,7.5*inch
NAVY=HexColor('#101C30'); NAVY2=HexColor('#172941'); PANEL=HexColor('#1C304A'); GOLD=HexColor('#C7A76B'); IVORY=HexColor('#F4F0E7'); MUTED=HexColor('#B9C5D2'); PALE=HexColor('#E1D2AE'); TEAL=HexColor('#83B5B0'); CORAL=HexColor('#D78D77')
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; SERIF='/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'
for name,path in [('Sans',FONT),('SansBold',BOLD),('Serif',SERIF)]:
    if os.path.exists(path): pdfmetrics.registerFont(TTFont(name,path))

def S(title, bullets, takeaway, kind='flow'):
    return {'title':title,'bullets':bullets,'takeaway':takeaway,'kind':kind}
modules=[
('01','Welcome & course orientation','A purposeful start: what AI is, why it matters, and how this course connects to robotics.',[
S('Welcome to AI.101',['Bachelor of Artificial Intelligence and Robotics Engineering','Course: Introduction to Artificial Intelligence · 2.70 credits','A foundation for thinking clearly about intelligent systems'],'Begin with questions, evidence, and responsible curiosity.','hero'),
S('The promise of this course',['Build a usable vocabulary for AI','Recognize major AI approaches and where they fit','Connect data, models, decisions, and physical action'],'AI is a family of methods—not one magic machine.','cards'),
S('Learning outcomes',['Explain core AI concepts in your own words','Trace a simple AI system from input to output','Compare rule-based and learning-based approaches','Identify risks, limitations, and human responsibilities'],'Understanding comes before implementation.','ladder'),
S('Where AI.101 sits in the degree',['Year 1: foundations in AI, robotics, learning, vision, language, and control','Year 2: perception, autonomous systems, deep learning, and kinematics','Years 3–4: integration, learning, manipulation, ethics, and capstone work'],'This course gives later technical courses a shared foundation.','timeline'),
S('A map of the discipline',['Perception: interpret signals from the world','Reasoning: represent facts and draw conclusions','Learning: improve behavior from experience or data','Action: choose and execute a response'],'A complete system links sensing, thinking, and doing.','cycle'),
S('How to learn from this presentation',['Pause at each “think” prompt before revealing the answer','Sketch diagrams by hand; explain them aloud','Keep a running glossary of unfamiliar terms','Treat examples as starting points for inquiry'],'Active recall makes concepts more durable.','cards'),
S('Nine-hour learning rhythm',['Nine guided learning blocks, one per hour','Each block mixes explanation, visual walkthrough, reflection, and knowledge check','Pause between blocks; use the activities rather than watching passively'],'The schedule is designed for paced orientation—not nine hours of uninterrupted talking.','timeline'),
S('Course norms: rigor and humility',['Ask what evidence supports a claim','Distinguish a model’s output from ground truth','Name uncertainty rather than hiding it','Respect people affected by automated decisions'],'Good engineering combines capability with accountability.','compare'),
S('Opening reflection: where do you meet AI?',['Name one system you use that may contain AI','What does it take as input?','What does it produce or influence?','What could go wrong if its output is wrong?'],'Start with the system’s role and consequences.','activity'),
S('Hour 1 synthesis',['AI is a broad field with many approaches','The degree connects algorithms to embodied machines','Clear questions and disciplined evidence are our starting tools'],'Next: define artificial intelligence carefully.','recap')]),
('02','What is artificial intelligence?','Definitions, agents, environments, goals, and the boundary between AI and ordinary automation.',[
S('A working definition',['AI studies computational systems that perform tasks associated with intelligent behavior','Tasks include perception, prediction, language, planning, and decision support','Definitions evolve as capabilities and expectations change'],'Define the task and context before labeling a system “intelligent.”','concept'),
S('Intelligence is not one score',['Different tasks require different capabilities','Competence in one setting does not imply general competence','Human intelligence includes social, physical, and contextual dimensions'],'Measure the capability that matters for the application.','compare'),
S('Agent and environment',['An agent receives observations through sensors or data inputs','It selects actions through an actuator, interface, or recommendation','The environment changes in response, producing new observations'],'An agent is defined by its interaction loop.','cycle'),
S('A simple agent loop',['Observe: collect the current state or signal','Interpret: estimate what is happening','Choose: select an action using rules or a model','Act and evaluate: observe what changed'],'Feedback closes the loop.','flow'),
S('Task environments',['Fully or partially observable','Deterministic or stochastic','Episodic or sequential','Static or changing; single-agent or multi-agent'],'Environment properties shape which methods are suitable.','matrix'),
S('AI, automation, and software',['Automation follows prescribed procedures for repeatable tasks','AI methods infer, search, learn, or reason under variation','Many products combine conventional software with AI components'],'Not every automated feature is AI.','compare'),
S('Narrow capability and generality',['Most deployed AI is designed for bounded tasks','A system can be highly capable and still fail outside its design conditions','Broad general intelligence remains a contested research concept'],'Avoid inferring general understanding from narrow performance.','spectrum'),
S('Case: a campus help assistant',['Inputs: student question and approved knowledge sources','Process: retrieve relevant material and compose a response','Output: answer that may guide a student decision','Safeguards: source links, escalation, and correction path'],'Useful answers need provenance and a human route for unresolved cases.','case'),
S('Think: is it AI?',['A thermostat switching at a fixed threshold','A camera classifying plant disease from images','A spreadsheet calculating a known formula','A robot adapting its route from sensor readings'],'Discuss: what makes each case fixed, inferred, or adaptive?','activity'),
S('Hour 2 synthesis',['AI is best understood through tasks, methods, and operating conditions','Agents connect observation to action','The environment determines what success and failure mean'],'Next: follow AI’s history through changing ideas and tools.','recap')]),
('03','A brief history of AI','From symbolic reasoning and expert systems to statistical learning and foundation models.',[
S('Why study AI history?',['Ideas return in new technical forms','Progress depends on data, compute, algorithms, and expectations','Historical cycles teach caution about exaggerated promises'],'History helps separate durable ideas from temporary hype.','hero'),
S('Early questions and formal roots',['Can reasoning be represented as symbol manipulation?','Can computation solve problems through search?','How should a machine’s behavior be evaluated?','Logic, mathematics, and early computing shaped the field'],'AI grew from several disciplines, not a single invention.','timeline'),
S('Symbolic AI and search',['Represent states, actions, and goals explicitly','Explore candidate paths through a search space','Use heuristics to prioritize promising possibilities'],'Explicit representations can be interpretable, but brittle when the world is messy.','flow'),
S('Knowledge-based systems',['Expert knowledge encoded as facts and rules','Inference engines apply rules to reach conclusions','Useful in constrained domains with accessible expertise'],'Knowledge acquisition and maintenance became major bottlenecks.','cycle'),
S('Learning from data',['Statistical methods estimate patterns from examples','Features translate raw data into useful measurements','Evaluation tests whether patterns generalize beyond training cases'],'The shift made data quality and evaluation central.','ladder'),
S('Neural networks and deep learning',['Layered networks learn representations from data','More data and compute enabled larger models','Deep learning advanced speech, vision, and language tasks'],'Scale can improve performance, but does not remove uncertainty.','network'),
S('Modern generative models',['Models learn statistical structure from large datasets','They generate plausible sequences, images, audio, or code','Plausibility is not the same as factual correctness'],'Generated output must be checked against trusted evidence.','flow'),
S('Recurring AI winters and hype',['Expectations can outrun reliable capability','Funding and attention shift as results disappoint or improve','Benchmark gains do not automatically translate into safe deployment'],'Ask what works, for whom, and under what conditions.','timeline'),
S('Timeline activity',['Place symbolic reasoning, expert systems, statistical learning, deep learning, and generative AI in order','For each era, name one enabling factor','Identify one limitation that persisted'],'Technology changes; the need for careful testing persists.','activity'),
S('Hour 3 synthesis',['AI history is a sequence of representations, methods, and enabling conditions','Each approach solves some problems and struggles with others','Progress is neither linear nor guaranteed'],'Next: inspect the anatomy of an AI system.','recap')]),
('04','How AI systems are built','Data, representations, algorithms, models, training, inference, evaluation, and deployment.',[
S('From problem to system',['Specify a real user need and decision context','Define what the system may and may not do','Choose measurable outcomes and acceptable risks'],'A well-framed problem is half the engineering work.','flow'),
S('Data: observations with a purpose',['Collect only data relevant to the task','Record provenance, permissions, and collection conditions','Check missing values, imbalance, errors, and sensitive attributes'],'Data quality is contextual, not just numerical cleanliness.','cards'),
S('Representations and features',['Raw signals may need transformation before a method can use them','Features summarize patterns relevant to a task','Learned representations are produced by training rather than hand-designed rules'],'Representation choices shape what a model can notice.','flow'),
S('Algorithm, model, and parameters',['An algorithm is a procedure for learning or solving','A model is the resulting structured predictor or decision process','Parameters encode what training has fitted'],'Keep the learning procedure distinct from the learned artifact.','compare'),
S('Training and inference',['Training adjusts model parameters using examples and an objective','Validation supports model and setting choices','Inference applies the trained model to new inputs'],'Training learns; inference uses what was learned.','cycle'),
S('Evaluation beyond one accuracy number',['Choose metrics tied to the actual decision','Test on data not used to fit the model','Examine subgroup performance, error types, and uncertainty'],'A metric is useful only when its meaning is understood.','matrix'),
S('Deployment is part of the system',['Integrate the model with interfaces and workflows','Monitor changing inputs and outcomes','Plan for versioning, rollback, incident response, and human escalation'],'A model is not a product until its surrounding system works.','lifecycle'),
S('Data leakage and misleading tests',['Leakage lets information from the answer or future enter training','Repeated tuning on a test set weakens the test’s independence','Distribution shift changes how inputs differ after deployment'],'A clean evaluation asks a genuinely new question.','warning'),
S('Walkthrough: plant-health classifier',['Capture leaf images under varied lighting and backgrounds','Label disease categories with expert review','Train and validate; inspect false negatives by class','Deploy with confidence thresholds and expert referral'],'The operating workflow matters as much as the classifier.','case'),
S('Hour 4 synthesis',['AI systems combine data, methods, people, and infrastructure','Evaluation must reflect context and consequences','Deployment requires monitoring and a plan for failure'],'Next: compare major AI approaches.','recap')]),
('05','Major AI approaches','Rules, search, knowledge representation, machine learning, reinforcement learning, and generative methods.',[
S('A family of approaches',['Rule-based reasoning uses explicit conditions','Search explores candidate states or actions','Machine learning estimates patterns from examples','Hybrid systems combine methods'],'Choose by task constraints, not trendiness.','taxonomy'),
S('Rules and logic',['Rules can encode policies or expert knowledge directly','Logical inference can make the reasoning path explicit','Exceptions and uncertainty can make rule sets hard to maintain'],'Rules work best when conditions are stable and expressible.','flow'),
S('Search and planning',['Define an initial state, available actions, and goal test','Explore possible sequences of actions','Use costs or heuristics to manage the search'],'Search is powerful when states and transitions are sufficiently modeled.','tree'),
S('Knowledge representation',['Represent entities, properties, relations, or constraints','Use ontologies or graphs to organize domain concepts','Reason over explicit relationships'],'Representation quality limits the conclusions that follow.','network'),
S('Supervised learning',['Learn a mapping from inputs to labeled examples','Classification predicts categories; regression predicts numeric values','Training data should represent intended use conditions'],'Labels encode human choices and may carry human error.','flow'),
S('Unsupervised and self-supervised learning',['Find structure without task labels, such as clusters','Learn useful representations from relationships within data','Results require interpretation and task-specific validation'],'Discovered structure is not automatically meaningful.','compare'),
S('Reinforcement learning',['An agent acts and receives reward signals','Learning balances short-term outcomes and future returns','Reward design can create unintended behavior'],'The reward is a proxy for goals, not the goal itself.','cycle'),
S('Generative methods and hybrids',['Generate new content conditioned on prompts or context','Combine retrieval, rules, and models for grounded behavior','Apply filters, provenance, and review where consequences matter'],'Generation expands capability but needs verification.','matrix'),
S('Approach-selection workshop',['Specify task, data availability, and cost of errors','Select a candidate method and explain why','Name one alternative and one test that could change your choice'],'Method selection is an argument supported by evidence.','activity'),
S('Hour 5 synthesis',['Rules, search, learning, and generation are complementary tools','Each approach has assumptions and failure modes','Hybrid architectures can allocate different tasks to suitable components'],'Next: connect AI to embodied systems and society.','recap')]),
('06','AI in robotics and the real world','Sensing, perception, planning, control, deployment, and cross-sector applications.',[
S('From digital model to physical action',['A robot senses a changing physical world','Software turns signals into estimates and choices','Actuators turn decisions into forces and motion'],'Physical AI must account for time, uncertainty, and safety.','hero'),
S('The sense–think–act loop',['Sense: camera, range sensor, encoder, or touch','Estimate: infer objects, position, and state','Plan: choose a feasible action','Act: move and measure the result'],'The loop repeats as the world changes.','cycle'),
S('Perception and sensor fusion',['Sensors provide different views of the world','Calibration relates measurements to a common frame','Fusion combines evidence while preserving uncertainty'],'More sensors help only when their limits are understood.','network'),
S('Planning and control are distinct',['Planning proposes a goal-directed sequence','Control computes commands that track the plan','Feedback corrects deviations caused by disturbance or model error'],'Plans describe intent; controllers manage execution.','compare'),
S('Examples across sectors',['Agriculture: monitor crops and support precision tasks','Healthcare: assist clinicians or support rehabilitation','Industry: inspect, move, and collaborate on production lines','Logistics: perceive, route, and handle goods'],'Applications should start with an actual user and context.','cards'),
S('Human oversight and autonomy',['Autonomy is a design choice on a continuum','Humans may supervise, approve, intervene, or take over','Interface design determines whether oversight is meaningful'],'A nominal human-in-the-loop is not enough; the person needs time and information.','spectrum'),
S('Reliability in the physical world',['Lighting, surfaces, wear, and obstacles alter sensor data','Latency and hardware faults affect control','Safe behavior may require conservative fallback modes'],'Test in conditions that resemble deployment.','warning'),
S('Case: indoor delivery robot',['Map corridors and identify restricted areas','Estimate location from sensors and map','Plan a route around people and temporary obstacles','Stop or request help when confidence or safety limits are crossed'],'A safe system knows when not to proceed.','case'),
S('Design a robot application',['Choose a setting and a user need','Sketch sensors, state estimate, planner, controller, and human interface','Mark one hazard and a mitigation'],'Good robotics begins with task and hazard analysis.','activity'),
S('Hour 6 synthesis',['Robotics couples AI with sensing, mechanics, and control','Uncertainty propagates from observation to action','Human context and safe fallback are part of the design'],'Next: practice responsibility, evaluation, and critical reflection.','recap')]),
('07','Strengths, limits & responsible use','Bias, privacy, explanation, uncertainty, safety, human oversight, and responsible innovation.',[
S('Capability and consequence',['An accurate prediction can still be misused','A low-probability error may have severe consequences','Assess who benefits, who bears risk, and who can appeal'],'Technical performance is one part of responsible deployment.','concept'),
S('Bias and representation',['Historical data may reflect unequal access or treatment','Sampling can omit communities or unusual conditions','Labels and categories embed assumptions'],'Audit the full pipeline, not just the model output.','flow'),
S('Privacy and data stewardship',['Collect only what is necessary','Protect sensitive information through access controls and retention limits','Explain data use and respect applicable consent and law'],'Privacy is a design requirement, not an afterthought.','cards'),
S('Explainability and transparency',['Different users need different explanations','A feature attribution is not a complete causal explanation','Communicate limitations, intended use, and confidence honestly'],'Explanations should support a real decision.','compare'),
S('Uncertainty and calibration',['A model can be uncertain even when it returns a confident-looking answer','Calibration compares stated confidence with observed correctness','Thresholds should reflect the cost of errors'],'Uncertainty can guide escalation and abstention.','spectrum'),
S('Safety and robustness',['Test normal, edge, and adversarial conditions','Use safeguards, constraints, monitoring, and fail-safe modes','Document hazards and incident response'],'Safety is built through layers, not a single feature.','matrix'),
S('Human accountability',['Assign a responsible owner for decisions and updates','Ensure people can contest or correct consequential outputs','Keep an audit trail proportionate to risk'],'Automation does not erase institutional responsibility.','lifecycle'),
S('Case: an automated admissions aid',['Potential benefit: organize large application queues','Risks: proxy discrimination, inaccessible data, opaque rankings','Controls: human review, validity testing, appeal route, monitoring'],'A high-stakes tool needs unusually strong evidence and governance.','case'),
S('Responsible-AI review exercise',['Who is affected and what is the decision?','What evidence supports validity for this population?','What happens when the system is wrong?','Who can explain, contest, and repair harm?'],'If these questions lack answers, deployment is premature.','activity'),
S('Hour 7 synthesis',['Fairness, privacy, safety, and accountability are socio-technical','Model performance must be interpreted in context','Responsible practice asks who is affected and how harm is addressed'],'Next: apply the concepts in a guided design challenge.','recap')]),
('08','Guided activity & knowledge check','A practical, low-code system analysis that brings together the course concepts.',[
S('The design challenge',['Scenario: a greenhouse wants early warnings of crop stress','Goal: help staff prioritize inspection, not replace their judgment','Constraint: variable lighting, limited connectivity, and seasonal change'],'Design for a useful decision, not an impressive demo.','hero'),
S('Step 1 — Frame the problem',['Identify the user and decision','Define the intended benefit and what is out of scope','Specify success and unacceptable failure'],'A narrow, testable scope is a strength.','activity'),
S('Step 2 — Map inputs and outputs',['Possible inputs: images, temperature, humidity, staff observations','Output: prioritized alert with supporting evidence','Human action: inspect, confirm, or dismiss'],'Trace every output to a real user action.','flow'),
S('Step 3 — Choose an approach',['Rule thresholds may flag known conditions','A vision model may classify visible symptoms','A hybrid can combine sensor rules and image evidence'],'Select a baseline before adding complexity.','compare'),
S('Step 4 — Plan the data',['Sample crops, growth stages, weather, and lighting variation','Obtain expert labels and record uncertainty','Separate training and test data by plot or time to reduce leakage'],'The test should represent future conditions.','matrix'),
S('Step 5 — Define evaluation',['Measure missed stress cases as well as false alarms','Report performance by crop and condition','Track time-to-inspection and whether staff find alerts useful'],'Evaluate the decision workflow, not only the model.','ladder'),
S('Step 6 — Add safeguards',['Show uncertainty and reasons for alerts','Allow staff to override and record corrections','Escalate low-confidence cases; monitor seasonal drift'],'Safeguards make the system safer and more useful.','warning'),
S('Knowledge check',['What distinguishes training from inference?','Why is a held-out test set important?','Name one source of data bias','Why should a robot or AI system sometimes abstain?'],'Pause and answer before viewing the next slide.','quiz'),
S('Answer key & discussion',['Training fits parameters; inference applies the fitted model','Held-out data estimates generalization to unseen examples','Sampling, labels, or historical decisions can introduce bias','Abstention can reduce harm when evidence is insufficient'],'Explain the reasoning, not only the answer.','answers'),
S('Hour 8 synthesis',['Frame the user decision before selecting a model','Evaluation and safeguards belong in the initial design','Human feedback can improve both system understanding and workflow'],'Next: consolidate the course and plan your next steps.','recap')]),
('09','Recap & next steps','Consolidate the core vocabulary, reflect, and connect AI.101 to the wider degree.',[
S('The AI system in one picture',['Problem context defines the task and acceptable outcomes','Data and representations make the task computational','Methods produce predictions, plans, or generated content','People deploy, evaluate, govern, and improve the system'],'The system includes its human and institutional setting.','lifecycle'),
S('Core vocabulary, part one',['Agent: system that selects actions from observations','Environment: world or context an agent interacts with','Model: structured method or learned representation','Training: fitting a model using data and an objective'],'Use terms consistently when discussing designs.','cards'),
S('Core vocabulary, part two',['Inference: applying a trained model to inputs','Feature: representation used to support a task','Metric: quantitative measure of a defined outcome','Distribution shift: changed input conditions after deployment'],'A metric needs context to become meaningful.','cards'),
S('Five questions for any AI system',['What task is being performed, and for whom?','What data and assumptions shape the output?','How was the system evaluated in relevant conditions?','What happens when it fails or is uncertain?','Who is accountable for outcomes and correction?'],'These questions travel across every AI specialization.','ladder'),
S('Common misconceptions to leave behind',['AI is not always learning or autonomous','High accuracy does not guarantee fairness or safety','Generated text can be fluent and still incorrect','A model alone is not the complete deployed system'],'Healthy skepticism is compatible with technical ambition.','compare'),
S('Your degree pathway',['AI.102–106: robotics, learning, vision, language, and control foundations','Year 2: perception, autonomy, reinforcement learning, and deep learning','Years 3–4: integrated systems, specialized robotics, ethics, and project work'],'Build fundamentals steadily; later courses connect them.','timeline'),
S('Personal reflection',['Which AI topic surprised you most?','What assumption about AI changed during this orientation?','What capability would you like to build responsibly?','What concept needs more study?'],'Curiosity becomes expertise through deliberate practice.','activity'),
S('Your first small investigation',['Choose an AI-enabled system you can observe','Describe inputs, outputs, users, and consequences','Find one claim about its performance and examine the evidence','Suggest one improvement or safeguard'],'Practice critical analysis on real systems around you.','activity'),
S('Closing knowledge check',['Explain AI in one careful sentence','Draw a sense–think–act or data-to-deployment diagram','Name one method, one evaluation concern, and one ethical risk','Connect AI.101 to one later course'],'A strong foundation is the ability to ask better questions.','quiz'),
S('Thank you — begin with purpose',['Observe systems carefully','Build with evidence and humility','Keep people and real-world context in view','Carry responsible practice into every technical course'],'Intelligence in motion begins with thoughtful engineers.','closing')])]

# Brief, original study/reference guidance (not a substitute for course readings)
appendix=[
S('Appendix A · Guided study plan',['Before class: preview key terms and write one question','During study: pause, sketch each system diagram, and retrieve concepts from memory','After study: explain one idea to a peer without reading the slide','Follow up: consult instructor-provided readings and laboratory materials'],'Use this deck alongside the university’s approved syllabus and readings.','cards'),
S('Appendix B · Glossary: foundations',['Agent: decision-making system interacting with an environment','Environment: external context that provides observations and receives actions','Algorithm: defined procedure for solving a problem or learning','Model: structured predictor, representation, or decision process'],'Precise language improves both learning and engineering communication.','cards'),
S('Appendix C · Glossary: learning',['Dataset: organized examples used for development or evaluation','Feature: input representation relevant to a task','Label: target annotation associated with an example','Generalization: performance on relevant unseen examples'],'Labels and datasets require documentation and scrutiny.','cards'),
S('Appendix D · Glossary: deployment',['Inference: applying a model to new input','Distribution shift: change in data conditions over time or context','Calibration: agreement between confidence and observed correctness','Fallback: safer alternative when system conditions are not met'],'Deployment introduces new conditions that must be monitored.','cards'),
S('Appendix E · Responsible-design checklist',['Purpose and affected people are clearly described','Data rights, privacy, and provenance are addressed','Testing matches the use context and includes error analysis','Human review, correction, and incident handling are defined'],'Do not treat this checklist as legal or regulatory advice.','matrix'),
S('Appendix F · Reflection prompts',['What is the simplest baseline that could meet the need?','Which error would be most harmful, and to whom?','What evidence would make you change the design?','When should the system stop, defer, or ask a person?'],'Use reflection to uncover hidden assumptions.','activity'),
S('Appendix G · Suggested next steps',['Review course-specific syllabus, readings, and assessment guidance','Strengthen programming, mathematics, and scientific communication','Practice data visualization and experimental design','Bring questions to instructors and lab sessions'],'This presentation is an orientation resource, not an official assessment specification.','timeline'),
S('Appendix H · Source and integrity note',['Explanations and diagrams in this deck are original instructional synthesis','Examples are illustrative and should not be treated as product endorsements','Verify current technical, legal, and institutional guidance before deployment','Consult instructor-approved texts and references for formal study'],'Claims are intentionally framed as introductory, not exhaustive.','cards'),
S('Final slide · A principled beginning',['Understand the task','Question the evidence','Design for people and context','Build systems that can be evaluated and corrected'],'TRIUNE BIBLICAL UNIVERSITY GLOBAL EXTENSION USA','closing')]

# drawing helpers
def rr(c,x,y,w,h,r,fill,stroke=None,lw=1):
    c.setLineWidth(lw); c.setFillColor(fill); c.setStrokeColor(stroke or fill); c.roundRect(x,y,w,h,r,fill=1,stroke=bool(stroke))
def text(c,s,x,y,size=14,color=IVORY,font='Sans'):
    c.setFillColor(color); c.setFont(font,size); c.drawString(x,y,s)
def wrap(s,font,size,maxw):
    words=s.split(); lines=[]; cur=''
    for word in words:
        test=(cur+' '+word).strip()
        if stringWidth(test,font,size)<=maxw: cur=test
        else:
            if cur: lines.append(cur)
            cur=word
    if cur: lines.append(cur)
    return lines
def para(c,s,x,y,maxw,size=13,color=IVORY,font='Sans',leading=None,maxlines=5):
    leading=leading or size*1.42
    lines=wrap(s,font,size,maxw)[:maxlines]
    c.setFillColor(color); c.setFont(font,size)
    for i,line in enumerate(lines): c.drawString(x,y-i*leading,line)
    return y-len(lines)*leading

def arrow(c,x1,y1,x2,y2,color=GOLD):
    c.setStrokeColor(color); c.setFillColor(color); c.setLineWidth(1.5); c.line(x1,y1,x2,y2)
    a=math.atan2(y2-y1,x2-x1); l=7
    p=c.beginPath(); p.moveTo(x2,y2); p.lineTo(x2-l*math.cos(a-.45),y2-l*math.sin(a-.45)); p.lineTo(x2-l*math.cos(a+.45),y2-l*math.sin(a+.45)); p.close()
    c.drawPath(p,fill=1,stroke=0)

def visual(c,kind,x,y,w,h,slide):
    # right-side editorial diagram panel
    rr(c,x,y,w,h,14,PANEL,HexColor('#29415C'),.8)
    c.setStrokeColor(Color(.78,.65,.42,alpha=.3)); c.setLineWidth(.6); c.line(x+17,y+h-38,x+w-17,y+h-38)
    text(c,'VISUAL MODEL',x+18,y+h-27,8,GOLD,'SansBold')
    cx=x+w/2; cy=y+h/2-7
    if kind in ('cycle','lifecycle'):
        labels=['OBSERVE','INTERPRET','DECIDE','ACT']
        pts=[(cx,cy+65),(cx+75,cy),(cx,cy-65),(cx-75,cy)]
        for i,((px,py),lab) in enumerate(zip(pts,labels)):
            rr(c,px-38,py-17,76,34,8,NAVY2,GOLD,.8); text(c,lab,px-stringWidth(lab,'SansBold',8)/2,py-3,8,IVORY,'SansBold')
            q=pts[(i+1)%4]; arrow(c,px+(q[0]-px)*.55,py+(q[1]-py)*.55,q[0]-(q[0]-px)*.36,q[1]-(q[1]-py)*.36,TEAL)
        text(c,'feedback updates the next step',cx-81,y+24,9,MUTED,'Sans')
    elif kind in ('flow','hero','concept','warning'):
        labels=slide.get('nodes',['INPUT','MODEL','OUTPUT'])
        if len(labels)>4: labels=labels[:4]
        gap=10; bw=(w-40-gap*(len(labels)-1))/len(labels); by=cy-17
        for i,label in enumerate(labels):
            xx=x+20+i*(bw+gap); rr(c,xx,by,bw,38,7,NAVY2,GOLD if i==1 else HexColor('#49617A'),.8)
            parts=wrap(label,'SansBold',7,bw-8)
            for j,line in enumerate(parts[:2]): text(c,line,xx+(bw-stringWidth(line,'SansBold',7))/2,by+22-j*10,7,IVORY,'SansBold')
            if i<len(labels)-1: arrow(c,xx+bw+1,cy,xx+bw+gap-2,cy)
        text(c,'A system is a chain of choices and evidence.',x+20,y+35,9,MUTED)
    elif kind in ('timeline','spectrum','ladder'):
        yy=cy+48 if kind!='ladder' else cy-63
        c.setStrokeColor(GOLD); c.setLineWidth(2); c.line(x+38,yy,x+w-38,yy)
        labels=slide.get('nodes',['FOUNDATION','METHOD','EVIDENCE','USE'])[:4]
        n=len(labels)
        for i,label in enumerate(labels):
            px=x+40+i*(w-80)/max(1,n-1); c.setFillColor(GOLD); c.circle(px,yy,5,fill=1,stroke=0)
            para(c,label,px-38,yy-22,76,7,IVORY,'SansBold',9,2)
        para(c,'Progress depends on context, evidence, and iteration.',x+24,y+47,w-48,9,MUTED,'Sans',13,3)
    elif kind in ('compare','matrix','taxonomy','cards','quiz','answers','activity','case','recap','closing'):
        labels=slide.get('nodes',['CONTEXT','METHOD','EVIDENCE','IMPACT'])[:4]
        cols=2; rows=2; gap=10; bw=(w-48)/2; bh=58
        for i,label in enumerate(labels):
            col=i%2; row=i//2; xx=x+16+col*(bw+10); yy=cy+43-row*(bh+10)-bh
            rr(c,xx,yy,bw,bh,8,NAVY2,HexColor('#49617A'),.7)
            c.setFillColor(GOLD); c.circle(xx+13,yy+bh-15,3,fill=1,stroke=0)
            para(c,label,xx+23,yy+bh-13,bw-31,8,PALE,'SansBold',10,3)
        text(c,'ASK  →  TEST  →  REFLECT',x+20,y+24,8,TEAL,'SansBold')
    elif kind=='network':
        points=[(cx,cy+62),(cx-62,cy+15),(cx+62,cy+15),(cx-40,cy-48),(cx+40,cy-48),(cx,cy)]
        edges=[(0,1),(0,2),(1,3),(1,5),(2,4),(2,5),(3,5),(4,5)]
        c.setStrokeColor(HexColor('#567089')); c.setLineWidth(1)
        for a,b in edges:c.line(*points[a],*points[b])
        for i,(px,py) in enumerate(points):c.setFillColor(GOLD if i==5 else TEAL);c.circle(px,py,7 if i==5 else 5,fill=1,stroke=0)
        text(c,'signals become relationships',cx-78,y+26,9,MUTED)
    elif kind=='tree':
        levels=[[(cx,cy+67)],[(cx-59,cy+23),(cx+59,cy+23)],[(cx-84,cy-27),(cx-35,cy-27),(cx+35,cy-27),(cx+84,cy-27)]]
        c.setStrokeColor(HexColor('#526A81')); c.setLineWidth(1)
        for i in range(2):
            for a in levels[i]:
                for b in levels[i+1]:
                    if abs(a[0]-b[0])<75:c.line(*a,*b)
        for row in levels:
            for px,py in row:c.setFillColor(GOLD if py==cy+67 else TEAL);c.circle(px,py,5,fill=1,stroke=0)
        text(c,'candidate states → goal',cx-68,y+25,9,MUTED)
    else:
        text(c,'Observe',x+28,cy,10,PALE); arrow(c,x+86,cy,x+120,cy); text(c,'Interpret',x+128,cy,10,PALE); arrow(c,x+185,cy,x+218,cy); text(c,'Act',x+226,cy,10,PALE)
    # source-like annotation
    para(c,slide.get('visual_note','Conceptual illustration · not to scale'),x+18,y+10,w-36,7,MUTED,'Sans',9,2)

def footer(c,page,total,section):
    c.setStrokeColor(Color(.78,.65,.42,alpha=.62)); c.setLineWidth(.65); c.line(38,28,W-38,28)
    text(c,'TRIUNE BIBLICAL UNIVERSITY GLOBAL EXTENSION USA',40,13,7.2,PALE,'SansBold')
    text(c,'AI.101  ·  INTRODUCTION TO ARTIFICIAL INTELLIGENCE',W/2-111,13,6.5,MUTED)
    text(c,f'{page:03d} / {total:03d}',W-87,13,7.5,GOLD,'SansBold')

def draw_cover(c,page,total):
    c.setFillColor(NAVY); c.rect(0,0,W,H,fill=1,stroke=0)
    # decorative orbit arcs
    c.saveState(); c.setStrokeColor(Color(.78,.65,.42,alpha=.27)); c.setLineWidth(1)
    for r in [100,145,190,235]: c.circle(W-110,H/2+7,r,stroke=1,fill=0)
    c.setStrokeColor(Color(.52,.71,.69,alpha=.5)); c.setLineWidth(2); c.circle(W-110,H/2+7,5,stroke=0,fill=1); c.restoreState()
    text(c,'TRIUNE BIBLICAL UNIVERSITY',56,H-64,11,PALE,'SansBold')
    text(c,'GLOBAL EXTENSION · USA',56,H-83,8.5,MUTED,'Sans')
    c.setFillColor(GOLD); c.rect(56,H-120,54,2,fill=1,stroke=0)
    text(c,'BACHELOR OF ARTIFICIAL INTELLIGENCE',56,H-158,10,GOLD,'SansBold')
    text(c,'& ROBOTICS ENGINEERING',56,H-175,10,GOLD,'SansBold')
    c.setFillColor(IVORY); c.setFont('Serif',39); c.drawString(54,H-250,'Introduction to')
    c.setFont('Serif',46); c.drawString(54,H-306,'Artificial Intelligence')
    text(c,'AI.101  ·  ORIENTATION LECTURE',57,H-351,11,PALE,'SansBold')
    para(c,'A guided foundation in intelligent agents, AI methods, learning systems, robotics, and responsible practice.',57,H-395,550,14,MUTED,'Sans',21,3)
    rr(c,57,88,160,34,7,PANEL,GOLD,.8); text(c,'NINE-HOUR LEARNING JOURNEY',69,101,8.2,PALE,'SansBold')
    footer(c,page,total,'Opening'); c.showPage()

def draw_slide(c, data, page,total,section,number):
    c.setFillColor(NAVY); c.rect(0,0,W,H,fill=1,stroke=0)
    # top label and section marker
    text(c,'AI.101  /  '+section.upper(),42,H-40,8.2,GOLD,'SansBold')
    text(c,f'{number:02d}',W-67,H-44,20,Color(.78,.65,.42,alpha=.55),'Serif')
    # title
    title=data['title']; sz=25 if len(title)<35 else 21
    text(c,title,42,H-82,sz,IVORY,'Serif')
    c.setFillColor(GOLD); c.rect(42,H-99,42,2,fill=1,stroke=0)
    # content left: three or four bullet statements
    leftx=50; y=H-136; maxw=5.5*inch
    for i,b in enumerate(data['bullets']):
        c.setFillColor(GOLD if i==0 else TEAL); c.circle(leftx+4,y-3,3,fill=1,stroke=0)
        end=para(c,b,leftx+18,y,maxw-18,12.2,IVORY,'Sans',17,4)
        y=end-15
    # takeaway
    boxy=52; boxh=76
    rr(c,42,boxy,5.85*inch,boxh,9,NAVY2,HexColor('#344B63'),.6)
    text(c,'KEY IDEA',56,boxy+55,7.5,GOLD,'SansBold')
    para(c,data['takeaway'],56,boxy+38,5.3*inch,11.1,PALE,'Sans',15,2)
    # timeline chip
    rr(c,42,H-119,66,17,6,PANEL,None)
    text(c,f'HOUR {section[:2]}',51,H-114,7.2,TEAL,'SansBold')
    visual(c,data.get('kind','flow'),W-4.95*inch-42,68,4.95*inch,H-160,data)
    footer(c,page,total,section); c.showPage()

def main():
    total=1+sum(len(m[3]) for m in modules)+len(appendix)
    c=canvas.Canvas(OUT,pagesize=(W,H),pageCompression=1)
    c.setTitle('AI.101 Introduction to Artificial Intelligence — Orientation Lecture')
    c.setAuthor('Triune Biblical University Global Extension USA')
    c.setSubject('Nine-hour guided orientation presentation for the Bachelor of Artificial Intelligence and Robotics Engineering')
    p=1; draw_cover(c,p,total); p+=1
    for code,title,desc,slides in modules:
        section=f'{code} · {title}'
        for i,s in enumerate(slides,1):
            # Add individualized diagram nodes from salient concepts where possible
            words=[w.strip('.,:;!?()') for w in title.upper().replace('&','').replace('—',' ').split() if len(w)>3]
            s.setdefault('nodes',words[:4] or ['INPUT','METHOD','EVIDENCE','OUTCOME'])
            draw_slide(c,s,p,total,section,i); p+=1
    for i,s in enumerate(appendix,1):
        s.setdefault('nodes',['PURPOSE','EVIDENCE','PEOPLE','ACTION'])
        draw_slide(c,s,p,total,'APPENDIX · STUDY & REFERENCE',i); p+=1
    c.save()
    print(f'Created {OUT}: {total} pages')
if __name__=='__main__': main()
