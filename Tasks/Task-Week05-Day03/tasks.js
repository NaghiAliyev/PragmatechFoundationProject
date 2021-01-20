userList=[
    {
        name:'Sabir',
        email:'sabir@mail.com',
        userTasks:[
            {
                taskName:'Task01',
                taskDeadline:2
            },
            {
                taskName:'Task02',
                taskDeadline:8
            },
            {
                taskName:'Task03',
                taskDeadline:10
            }

        ]
    },
    {
        name:'Hesen',
        email:'hesen.mail.com',
        userTasks:[
            {
                taskName:'XTask01',
                taskDeadline:2
            },
            {
                taskName:'XTask02',
                taskDeadline:15
            },
            {
                taskName:'XTask03',
                taskDeadline:4
            }

        ]
    }
]

function findUserTasksByName(userName){
    // istifadeci adini daxil etdiyim zaman o istifadecinin tasklarini gosteren function
    for(i=0;i<userList.length;i++){
        if(userName == userList[i].name){
            for(j=0;j<userList[i].userTasks.length;j++){
                console.log('Task name : ' + userList[i].userTasks[j].taskName)
                console.log('Task deadline : ' + userList[i].userTasks[j].taskDeadline)
            }
        }
    }
} 

function userEmailCheck(){
    // butun istifadecilerin mail adreslerinin duzgun olub olmadigini yoxlayin (mail daxilinde @ isaretinin olub olmamasi)
    // duzgun olmayan mail adresi varsa o mailin hansi istifadeciye aid oldugunu ekrana cap edin
    for(i=0;i<userList.length;i++){
        emailAddress=userList[i].email;
        if(emailAddress.search('@') == -1){
            console.log(emailAddress);
        }
    }
} 

function findLongestDeadline(){
    // en uzun deadlinea sahib olan taskin adini,muddetini ve o taskin hansi istifadeciye aid oldugunu ekrana cap edin
    luckyUser=userList[0];
    longestDeadline=luckyUser.userTasks[0].taskDeadline;
    indexOfLongestDeadLine=0;
    for(i=1;i<userList.length;i++){
        for(j=0;j<userList[i].userTasks.length;j++){
            if(longestDeadline<userList[i].userTasks[j].taskDeadline){
                luckyUser=userList[i];
                longestDeadline=luckyUser.userTasks[j].taskDeadline;
                indexOfLongestDeadLine=j;
            }
        }
    }
    console.log('The man who has the longest deadline : ' + luckyUser.name)
    console.log('The name of task with the longest deadline : ' + luckyUser.userTasks[indexOfLongestDeadLine].taskName)
    console.log('The longest deadline : ' + luckyUser.userTasks[indexOfLongestDeadLine].taskDeadline)
}
    