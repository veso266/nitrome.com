I have added theese 2 functions inside NitromeGame.as (also the game is not URL Locked)

```as3
public static function get GetScoreRetrieveUrl():String
{
    // Get parameter list
    var paramObj:Object = timeline.loaderInfo.parameters

    // Check if parameter exists
    if(paramObj.hasOwnProperty("ScoreRetrieveUrl") && paramObj["ScoreRetrieveUrl"] != "")
        return paramObj["ScoreRetrieveUrl"];                     
    else
        return NitromeGame.RETRIEVE_URL;
}

public static function get GetScoreSubmitUrl():String
{
    // Get parameter list
	var paramObj:Object = timeline.loaderInfo.parameters;

    // Check if parameter exists
    if(paramObj.hasOwnProperty("ScoreSubmitUrl") && paramObj["ScoreSubmitUrl"] != "")
        return paramObj["ScoreSubmitUrl"];                     
    else
        return NitromeGame.SUBMIT_URL;
}
public static function get GetScoreDecryptionKey():String
{
    // Get parameter list
	var paramObj:Object = timeline.loaderInfo.parameters;

    // Check if parameter exists
    if(paramObj.hasOwnProperty("ScoreDecryptionKey") && paramObj["ScoreDecryptionKey"] != "")
        return paramObj["ScoreDecryptionKey"];                     
    else
        return NitromeGame.ar_key;
}
```

to capture Flash arguments, example usage is in ```example.html``` or you can just pass theese 2 arguments to your game and enjoy
```
 ScoreRetrieveUrl = http://192.168.88.12/Nitrome/retrieve_scores.php
 ScoreSubmitUrl = http://192.168.88.12/Nitrome/submit_score.php
```