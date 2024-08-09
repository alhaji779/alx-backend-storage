-- ins=dex on score and fisrt name
CREATE INDEX idx_name_first_score on names (name(1), score);
