package retQSS_social_force_model_params

import retQSS_covid19_utils;

function PEDESTRIAN_A
	output Real pedestrianA;
algorithm
	pedestrianA := getRealModelParameter("PEDESTRIAN_A", 2.1);
end PEDESTRIAN_A;

function PEDESTRIAN_B
	output Real pedestrianB;
algorithm
	pedestrianB := getRealModelParameter("PEDESTRIAN_B", 0.3);
end PEDESTRIAN_B;

function PEDESTRIAN_R
	output Real pedestrianR;
algorithm
	pedestrianR := getRealModelParameter("PEDESTRIAN_R", 0.1);
end PEDESTRIAN_R;

function PEDESTRIAN_LAMBDA
	output Real pedestrianLambda;
algorithm
	pedestrianLambda := getRealModelParameter("PEDESTRIAN_LAMBDA", 0.3);
end PEDESTRIAN_LAMBDA;

function RELAXATION_TIME
	output Real relaxationTime;
algorithm
	relaxationTime := getRealModelParameter("RELAXATION_TIME", 0.5);
end RELAXATION_TIME;

function BORDER_A
	output Real borderA;
algorithm
	borderA := getRealModelParameter("BORDER_A", 100.0);
end BORDER_A;

function BORDER_B
	output Real borderB;
algorithm
	borderB := getRealModelParameter("BORDER_B", 0.2);
end BORDER_B;

function BORDER_R
	output Real borderR;
algorithm
	borderR := getRealModelParameter("BORDER_R", 0.01);
end BORDER_R;

end retQSS_social_force_model_params;