#[derive(Debug)]
pub enum SchedulerError {
    InvalidJob,
    TribeOverQuota,
    PlanetEmergencyViolation,
}