
    var cmd = "/Library/Frameworks/Python.framework/Versions/3.6/bin/python3 ~/dareiru/dareiru.py";
    var execSync = require('child_process').execSync;
    var result = execSync(cmd).toString();

    let dareiru = result.split(" ");


    var postData = `tuple={\"where\":\"delta\",\"type\":\"dareiru\",\"Who\":\"${dareiru}\"}`;

    cmd2= `curl -d '${postData}' URL`;
    execSync(cmd2);
