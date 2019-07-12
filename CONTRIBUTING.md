# How to contribute #

We'd love for you to contribute to rosetta-code-generators. There are
a just a few small guidelines  we would like you to follow:

 - [Code of Conduct](#coc)
 - [Issues and Bugs](#issue)
 - [Feature Requests](#feature)
 - [Submission Guidelines](#submit)
 - [Coding Rules](#rules)


## <a name="coc"></a> Code of Conduct
As contributors and maintainers of this project, we pledge to respect everyone who contributes by posting issues, updating documentation, submitting pull requests, providing feedback in comments, and any other activities.

Communication should be constructive and never resort to personal attacks, trolling, public or private harassment, insults, or other unprofessional conduct.

We promise to extend courtesy and respect to everyone involved in this project. We expect anyone contributing to do the same.

If any member of the community violates this code of conduct, the maintainers of this may take action, removing issues, comments, and PRs as deemed appropriate.

## <a name="issue"></a> Found a Bug?
If you find a bug in the source code, you can [submit an issue](#submit-issue) to our [GitHub Repository][github]. 
You can get more information about [github issues here].
Even better, you can [submit a Pull Request](#submit-pr) with a fix.

## <a name="feature"></a> Missing a Feature?
You can *request* a new feature by [submitting an issue](#submit-issue) to our GitHub
Repository. If you would like to *implement* a new feature, please submit an issue with
a proposal for your work first, to be sure that we can use it.

* For a **Major Feature**, first open an issue and outline your proposal so that it can be
discussed. This will also allow us to better coordinate our efforts, prevent duplication of work,
and help you to craft the change so that it is successfully accepted into the project.
* **Small Features** can be crafted and directly [submitted as a Pull Request](#submit-pr).

## <a name="submit"></a> Submission Guidelines

### <a name="submit-issue"></a> Submitting an Issue

Before you submit an issue, please search the issue tracker, maybe an issue for your problem already exists and the discussion might inform you of workarounds readily available.

We want to fix all the issues as soon as possible, but before fixing a bug we need to reproduce and confirm it. In order to reproduce bugs, we ask you to provide us with the necessary information, so that we act without going back & forth to you with additional questions.

A minimal reproduction allows us to quickly confirm a bug (or point out a coding problem) as well as confirm that we are fixing the right problem.

You can file new issues by selecting from our [new issue templates](https://github.com/REGnosys/rosetta-code-generators/issues/new/choose) and filling out the issue template.

### <a name="submit-pr"></a> Submitting a Pull Request (PR)
Before you submit your Pull Request (PR) consider the following guidelines:

1. Search [GitHub](https://github.com/REGnosys/rosetta-code-generators/pulls) for an open or closed PR
  that relates to your submission. You don't want to duplicate effort.
1. Be sure that an issue describes the problem you're fixing, or documents the design for the feature you'd like to add.
   Discussing the design up front helps to ensure that we're ready to accept your work.
1. Fork the REGnosys/rosetta-code-generators repo.
   [More information about forking]
1. Setup a new branch for your changes. 

     ```shell
     git checkout -b cool-feature-branch master
     ```

1. Create your patch, **including appropriate test cases**.
1. Follow our [Coding Rules](#rules).
1. Run the full build at the *parent* level of the project and ensure that all tests pass.

     ```shell
     ... rosetta-code-generators> mvn clean install
     ```

1. Commit your changes using [well-formed commit messages][]. This provides consistency throughout the project, 
    and ensures that commit messages are able to be formatted properly and used by various git tools.

     ```shell
     git commit -a
     ```
    Note: the optional commit `-a` command line option will automatically "add" and "rm" edited files.

1. Push your branch to GitHub:

    ```shell
    git push origin cool-feature-branch
    ```

1. In GitHub, create a [pull request] to `rosetta-code-generators:master` and choose as reviewer 
    a member of the team
* If we suggest changes then:
  * Make the required updates.
  * Re-run the build to ensure tests are still passing.
  * Rebase your branch and force push to your GitHub repository (this will update your Pull Request):

    ```shell
    git rebase master -i
    git push -f
    ```

That's it! Thank you for your contribution!

### After your pull request is merged

After your pull request is merged, you can safely delete your branch and pull the changes
from the main (upstream) repository:

* Delete the remote branch on GitHub either through the GitHub web UI or your local shell as follows:

    ```shell
    git push origin --delete cool-feature-branch
    ```

* Check out the master branch:

    ```shell
    git checkout master -f
    ```

* Delete the local branch:

    ```shell
    git branch -D cool-feature-branch
    ```

* Update your master with the latest upstream version:

    ```shell
    git pull --ff upstream master
    ```

## <a name="rules"></a> Coding Rules
To ensure consistency throughout the source code, keep these rules in mind as you are working:

* All public API methods **should be documented**.
* We format the code using a version of the built-in Eclipse java formatter (allows for 120 characters line length), which can be imported in both Eclipse and IntelliJ IDEA and check the build with matching [checkstyle rules]. At the moment this does not fail the build, but only produces warning messages; this can change in future releases.
  

[More information about forking]: https://help.github.com/articles/fork-a-repo
[well-formed commit messages]: http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html
[pull request]: https://help.github.com/articles/creating-a-pull-request
[github issues here]:https://guides.github.com/features/issues
[github]: https://github.com/REGnosys/rosetta-code-generators
[checkstyle rules]: https://github.com/REGnosys/rosetta-code-generators/tree/master/checkstyle/checkstyle.xml
