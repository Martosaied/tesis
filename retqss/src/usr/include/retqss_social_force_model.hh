#ifndef _RETQSS_SOCIAL_FORCE_MODEL_H_
#define _RETQSS_SOCIAL_FORCE_MODEL_H_

#include "retqss/retqss_types.hh"

#ifdef __cplusplus

#include <unordered_map>
#include <list>

#include <vector>
#include "retqss/retqss_cgal_main_types.hh"
#include "retqss/retqss_particle_neighbor.hh"
#include "retqss/retqss_particle_neighborhood.hh"

extern "C"
{
#endif

Bool social_force_model_setUpParticles(
    int N,
    double cellEdgeLength,
    int gridDivisions,
    double *x);

int social_force_model_setDebugLevel(int level);

Bool social_force_model_isDebugLevelEnabled(int level);

int social_force_model_debug(int level, double time, const char *format, int int1, int int2, double double1, double double2);

double social_force_model_arrayGet(double *array, int index);

Bool social_force_model_arraySet(double *array, int index, double value);

int social_force_model_getIntegerModelParameter(const char *name, int defaultValue);

double social_force_model_getRealModelParameter(const char *name, double defaultValue);

Bool social_force_model_isInArrayParameter(const char *name, int value);

Bool social_force_model_outputCSV(double time, 
	int N,
	double *x);

// void repulsive_pedestrian_effect(
// 	retQSS::ParticleNeighbor *neighbors,
// 	const std::vector<double> &args,
// 	Vector_3 &result);

void social_force_model_totalRepulsivePedestrianEffect(
	int particleID,
	double *desiredSpeed,
	double *pX,
	double *pY,
	double *pZ,
	double *pVX,
	double *pVY,
	double *pVZ,
	double targetX,
	double targetY,
	double *x,
	double *y,
	double *z);

void social_force_model_totalRepulsiveBorderEffect(
	int particleID,
	double pX[1],
	double pY[1],
	double pZ[1],
	double *x,
	double *y,
	double *z);

void social_force_model_acceleration(
	int particleID,
	double* desiredSpeed,
	double* px,
	double* py,
	double* pz,
	double* vx,
	double* vy,
	double* vz,
	double targetX,
	double targetY,
	double targetZ,
	double *x,
	double *y,
	double *z);

void social_force_model_desiredDirection(
	double currentX,
	double currentY,
	double currentZ,
	double targetX,
	double targetY,
	double targetZ,
	double *desiredX,
	double *desiredY,
	double *desiredZ);

#ifdef __cplusplus
}
#endif

#endif