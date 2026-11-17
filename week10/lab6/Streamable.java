public interface Streamable {
    void buffer();
    int getBitrate();
    
    //Activity 5: Quality Check
    default String getQualityStatus() {
        return (getBitrate() < 128) ? "Low Quality" : "High Definition";
    }
}